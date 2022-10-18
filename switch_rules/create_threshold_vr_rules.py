"""
线下用python3执行，读取threshold流量工程算出来的threshold矩阵
增加virtual r，分流按照一定比例
生成基于该矩阵的交换机配置项
"""
from switch_common import *
import sys
sys.path.append("../traffic")
import read_traffic as rt


def add_switch_rules(pod_num, which_row):
    """
    Desc: 根据dscp_remark_rate二维array来设置不同位置的threshold
    """
    
    threshold = rt.get_config(f'../traffic/{pod_num}pod_threshold.csv', which_row = which_row, pod_num = pod_num)

    virtual_r = rt.get_config(f'../traffic/{pod_num}pod_virtual_r.csv', which_row = which_row, pod_num = pod_num)
    # print(virtual_r)
    virtual_r = [float(r) for r in virtual_r[0]]
    # print(virtual_r)
    R = sum(virtual_r)

    rules_str = ''

    for src in range(1, pod_num + 1):
        for dst in range(1, pod_num + 1):
            if dst != src:
                rules_str += add_meter(f's{src}', dst, threshold[src - 1][dst - 1], 1) + '\n'
                # 根据目的地，选择走对应的限流meter表
                rules_str += add_gototable_flow(
                    switch_name = f's{src}',
                    table_id = 0,
                    in_port = src,
                    meter_id = dst,
                    goto = 1,
                    eth_dst='00:00:00:00:00:' + str(dst).rjust(2,'0'),
                ) + '\n'

                # 1跳routing
                rules_str += add_normal_flow(
                    switch_name = f's{src}',
                    table_id = 1,
                    match_dict = {
                        'in_port': str(src),
                        'eth_type': '0x800',
                        'eth_dst': '00:00:00:00:00:' + str(dst).rjust(2,'0'),
                        'ip_dscp': '2'
                    },
                    apply_dict = {
                        'output': str(dst)
                    }
                ) + '\n'

                # 返回流没有带--tos特殊标记，ip_dscp=0 直接走1跳
                rules_str += add_normal_flow(
                    switch_name = f's{src}',
                    table_id = 1,
                    match_dict = {
                        'in_port': str(src),
                        'eth_type': '0x800',
                        'eth_dst': '00:00:00:00:00:' + str(dst).rjust(2,'0'),
                        'ip_dscp': '0'
                    },
                    apply_dict = {
                        'output': str(dst)
                    }
                ) + '\n'

                # 2跳routing
                weight = []
                r_i = virtual_r[src - 1]
                r_j = virtual_r[dst - 1]
                for k in range(pod_num):
                    weight.append(100 * virtual_r[k] / (R - min(r_i, r_j)))

                rules_str += add_group(f's{src}', dst, src, dst, pod_num, weight) + '\n'
                rules_str += add_normal_flow(
                    switch_name = f's{src}',
                    table_id = 1,
                    match_dict = {
                        'in_port': str(src),
                        'eth_type': '0x800',
                        'eth_dst': '00:00:00:00:00:' + str(dst).rjust(2,'0'),
                        'ip_dscp': '4'
                    },
                    apply_dict = {
                        'group': str(dst)
                    }
                ) + '\n'


                for mid in range(1, pod_num + 1):
                    if mid != src and mid != dst:
                        # 中转交换机流向
                        rules_str += add_normal_flow(
                            switch_name = f's{mid}',
                            table_id = 0,
                            match_dict = {
                                'in_port': str(src),
                                'eth_dst': '00:00:00:00:00:' + str(dst).rjust(2,'0'),
                            },
                            apply_dict = {
                                'output': str(dst)
                            }
                        ) + '\n'
                    if mid != dst:
                        # 中转过来的流量流向目的地host
                        rules_str += add_normal_flow(
                            switch_name = f's{dst}',
                            table_id = 0,
                            match_dict = {
                                'in_port': str(mid),
                                'eth_dst': '00:00:00:00:00:' + str(dst).rjust(2,'0'),
                            },
                            apply_dict = {
                                'output': str(dst)
                            }
                        ) + '\n'       
    
    return rules_str

if __name__ == "__main__":
    pod_num = 4
    res = add_switch_rules(pod_num, 0)
    with open(f'./{pod_num}pod_threshold_vr_rules.sh', 'w') as f:
        f.write(res)