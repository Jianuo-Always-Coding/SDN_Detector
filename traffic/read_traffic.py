# -*- coding: utf-8 -*-

import math
import numpy as np

def get_traffic(file_name):
    with open(file_name, 'r') as f:
        row_list = f.read().splitlines()

    traffic_list = []
    for row in row_list:
        ori = row.split(',')
        pod_num = int(math.sqrt(len(ori)))
        a_traffic = []

        for i in range(pod_num):
            a_traffic.append(ori[i * pod_num : i * pod_num + pod_num])
        
        traffic_list.append(np.array(a_traffic).astype(int))
    
    return traffic_list


def get_config(file_name, which_row, pod_num = 4):
    """
    Desc: 获取threshold或topo或virtual_r的配置文件which_row行
    并转换为矩阵的 pod_num x pod_num 形式
    """
    with open(file_name, 'r') as f:
        row_list = f.read().splitlines()
    matrix = []
    ori = row_list[which_row].split(',')
    for i in range(pod_num):
        matrix.append(ori[i * pod_num : i * pod_num + pod_num])

    return matrix


if __name__ == "__main__":
    res = get_traffic('./4pod_traffic.csv')
    print(res[0:2])
    res = get_config('./4pod_threshold.csv', which_row = 0, pod_num = 4)
    print(res)