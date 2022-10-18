import handle_traffic as ht

def display_abnormal_traffic():
    for i in range(0, 80000, 1000):
        data = ht.get_col_traffic_by_window("../traffic/database_traffic.csv", 3, i, i + 1000)
        abnormal_list = ht.three_times_std_detect(data)
        print(abnormal_list)


if __name__ == "__main__":
    display_abnormal_traffic()
