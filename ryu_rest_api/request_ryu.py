"""
ryu的rest api控制器启动后，在外部对ryu发请求进而控制交换机
python3运行
"""
import requests

RYU_ADDR = 'localhost:8080'

def get_topology():
    return requests.get(f'http://{RYU_ADDR}/v1.0/topology/links').json()


def get_stats_flow(switch_id):
    return requests.get(f'http://{RYU_ADDR}/stats/flow/{switch_id}').json()[f'{switch_id}']


def get_group_desc(switch_id):
    return requests.get(f'http://{RYU_ADDR}/stats/groupdesc/{switch_id}').json()[f'{switch_id}']


def get_meter_config(switch_id):
    return requests.get(f'http://{RYU_ADDR}/stats/meterconfig/{switch_id}').json()[f'{switch_id}']


def get_stats_meter(switch_id):
    return requests.get(f'http://{RYU_ADDR}/stats/meter/{switch_id}').json()[f'{switch_id}']



if __name__ == "__main__":
    # print(get_topology())
    res = get_stats_flow(3)[1]
    print(res)