"""
线下用python3执行, 生成直连路由交换机配置项
"""
from switch_common import *

def add_switch_rules(pod_num):
    rules_str = ''

    for src in range(1, pod_num + 1):
        for dst in range(1, pod_num + 1):
            if dst != src:
                # 1跳routing
                rules_str += add_normal_flow(
                    switch_name = f's{src}',
                    table_id = 0,
                    match_dict = {
                        'in_port': str(src),
                        'eth_dst': '00:00:00:00:00:' + str(dst).rjust(2,'0'),
                    },
                    apply_dict = {
                        'output': str(dst)
                    }
                ) + '\n'

                rules_str += add_normal_flow(
                    switch_name = f's{dst}',
                    table_id = 0,
                    match_dict = {
                        'in_port': str(src),
                        'eth_dst': '00:00:00:00:00:' + str(dst).rjust(2,'0'),
                    },
                    apply_dict = {
                        'output': str(dst)
                    }
                ) + '\n'       
    
    return rules_str

if __name__ == "__main__":
    pod_num = 8
    res = add_switch_rules(pod_num)
    with open(f'./{pod_num}pod_direct_rules.sh', 'w') as f:
        f.write(res)