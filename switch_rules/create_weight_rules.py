"""
线下用python3执行，用group table进行不同比例的分流
生成基于该矩阵的交换机配置项
"""
from switch_common import *
import sys
sys.path.append("../traffic")
import read_traffic as rt


def add_switch_rules(pod_num, weight_file):
    

    rules_str = ''

    for src in range(1, pod_num + 1):
        for dst in range(1, pod_num + 1):
            if dst != src:
                # 2跳routing
                weight = []
                for k in range(pod_num):
                    weight.append(k + 100)  # test
                    # weight.append(100 * virtual_r[k] / (R - min(r_i, r_j)))

                rules_str += add_weight_group(f's{src}', dst, src, pod_num, weight) + '\n'
                rules_str += add_normal_flow(
                    switch_name = f's{src}',
                    table_id = 0,
                    match_dict = {
                        'in_port': str(src),
                        'eth_type': '0x800',
                        'eth_dst': '00:00:00:00:00:' + str(dst).rjust(2,'0'),
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
    res = add_switch_rules(pod_num, f'../traffic/{pod_num}pod_weight.csv')
    with open(f'./{pod_num}pod_weight_rules.sh', 'w') as f:
        f.write(res)