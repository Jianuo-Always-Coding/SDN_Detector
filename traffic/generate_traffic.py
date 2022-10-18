import numpy as np
import pandas as pd
np.random.seed(0)

# 出现0代表，该位置没有流量
# 出现[mean, std, min, max]表示该位置据此生成流量
TRAFFIC_PATTERN = [
    0, [700, 70, 500, 1000], [30, 30, 0, 100], [50, 20, 0, 100],
    [700, 70, 500, 1000], 0, [50, 30, 0, 100], [30, 30, 0, 100],
    [30, 30, 0, 100], [30, 30, 0, 100], 0, [30, 30, 0, 100],
    [30, 30, 0, 100], [30, 30, 0, 100], [30, 30, 0, 100], 0
]


def gen_random(mean, std, min, max, size = None):
    """
    Desc: 根据均值、标准差、最小值、最大值限定来产生随机数
    size = 3 表示产生3个随机数，返回值类型为 numpy.ndarray
    size = None 表示产生1个随机数，返回值类型为 numpy.int64
    """
    # 正态分布生成随机数, loc: 正态分布的均值, scale: 正态分布的标准差
    ret = np.random.normal(loc = mean, scale = std, size = size)
    ret = np.maximum(ret, min)
    ret = np.minimum(ret, max)
    ret = ret.astype(int)
    return ret


def gen_traffic(num):
    """
    Desc: 产生num行流量
    """
    traffic = None
    for ele in TRAFFIC_PATTERN:
        if ele == 0:
            traffic = np.zeros([num,1], dtype=int) if traffic is None else np.c_[traffic, np.zeros(num, dtype=int)]
            continue

        mean, std, min, max = ele
        traffic_col = gen_random(mean, std, min, max, num)
        traffic = np.c_[traffic, traffic_col]

    return traffic


if __name__ == "__main__":
    traffic = gen_traffic(100)
    res = pd.DataFrame(traffic)
    res.to_csv('4pod_traffic.csv', header=None, index=False)
