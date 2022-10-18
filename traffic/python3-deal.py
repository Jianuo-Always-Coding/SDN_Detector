"""
python3 运行处理npy，换成csv，方便python2读取
"""
import numpy as np

def get_ori_traffic_seq(file_name):
    """从某个历史流量矩阵文件中得到矩阵序列
    """
    traffic_history = np.load(file_name, allow_pickle = True)[0]
    
    traffic_seq = []
    for timestamp, traffic in traffic_history.items():
        # pod自己到自己的流量置0
        pod_num = traffic.shape[0]
        for i in range(pod_num):
            traffic[i][i] = 0
        traffic_seq.append(traffic / 300 * 8 / 1000000000)

    return np.array(traffic_seq)

if __name__ == "__main__":
    traffic_seq = get_ori_traffic_seq('./8pod_traffic.npy').astype(int)
    size = traffic_seq.shape[0]
    res = []
    for i in range(size):
        row = traffic_seq[i].astype(str).flatten().tolist()
        res.append(','.join(row))
   
    res_str = '\n'.join(res)  # 每行拼接
    with open('8pod_traffic.csv', 'w', encoding = 'utf-8') as f:
        f.write(res_str)

