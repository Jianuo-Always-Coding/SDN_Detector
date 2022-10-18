"""
线下用python3执行，添加clos结构的路由
从 aggregation 层的 core 层用group table随机选路
"""
from switch_common import *
import sys
sys.path.append("../traffic")
import read_traffic as rt


def add_switch_rules(pod_num):
    

    rules_str = ''

    for src in range(1, pod_num + 1):
        weight = []
        for k in range(pod_num):
            weight.append(100)  # test

        rules_str += add_weight_group(f's{src}', 0, src, pod_num, weight) + '\n'
        rules_str += add_normal_flow(
            switch_name = f's{src}',
            table_id = 0,
            match_dict = {
                'in_port': '5',
                'eth_type': '0x800',
            },
            apply_dict = {
                'group': '0'
            }
        ) + '\n'
        for dst in range(1, pod_num + 1):
            # core 交换机流表
            rules_str += add_normal_flow(
                switch_name = f'cs{src}',
                table_id = 0,
                match_dict = {
                    'eth_dst': '00:00:00:00:00:' + str(dst).rjust(2,'0'),
                },
                apply_dict = {
                    'output': str(dst)
                }
            ) + '\n'
    
        # core层过来的流量流向目的地host
        rules_str += add_normal_flow(
            switch_name = f's{src}',
            table_id = 0,
            match_dict = {
                'eth_dst': '00:00:00:00:00:' + str(src).rjust(2,'0'),
            },
            apply_dict = {
                'output': '5'
            }
        ) + '\n'       
    
    return rules_str

if __name__ == "__main__":
    pod_num = 4
    res = add_switch_rules(pod_num)
    with open(f'./{pod_num}pod_clos_rules.sh', 'w') as f:
        f.write(res)