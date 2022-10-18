import numpy as np
import pandas as pd


def get_ori_traffic(filename):
    return pd.read_csv(filename, header=None)


def get_col_traffic_by_window(filename, col_num, window_start = None, window_end = None):
    ori_traffic = get_ori_traffic(filename)
    if window_start == None:
        return ori_traffic.iloc[:,col_num]
    else:
        return ori_traffic.iloc[window_start : window_end, col_num]


def three_times_std_detect(data):
    data_mean = data.mean()
    data_std = data.std()
    abnormal_list = []
    for value in data:
        if abs(value - data_mean) > 3 * data_std:
            abnormal_list.append(value)
    return abnormal_list


if __name__ == "__main__":
    data = get_col_traffic_by_window("../traffic/database_traffic.csv", 3, 1000, 2000)
    three_times_std_detect(data)
