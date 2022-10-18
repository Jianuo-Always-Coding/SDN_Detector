import json
import sys
import os
import time

from mininet.net import Mininet
from mininet.node import RemoteController, OVSSwitch, UserSwitch
from mininet.cli import CLI
from mininet.link import TCLink, TCULink
from mininet.log import setLogLevel

from base_net import BaseNet
sys.path.append("../traffic")
sys.path.append("../config")
import read_traffic as rt
import run_config as rc


def topology(remoteip, ofversion, pod_num, which_row, traffic_num):
    topo_file = '../config/' + str(pod_num) + 'pod_topo.json'
    traffic_file = '../traffic/' + str(pod_num) + 'pod_traffic.csv'
    topo_bw = rt.get_config('../traffic/' + str(pod_num) + 'pod_topo.csv', which_row, pod_num)

    switch_rules_file = '../switch_rules/' + str(pod_num) + 'pod_clos_rules.sh'

    print('Runtime configuration:')
    print('The number of pod:', pod_num)
    print(topo_file)
    print('What is the line of the topo and threshold file: ', which_row)
    print(traffic_file)
    print(switch_rules_file)
    print('------')

    net = BaseNet(
        controller=RemoteController,
        switch=UserSwitch,
        autoStaticArp=True,
        link=TCULink,
    )
    c1 = net.addController("c1",controller=RemoteController,ip=remoteip,port=6653)
    switch_dict = {}
    switch_list = []

    with open(topo_file, 'r') as load_f:
        load_dict = json.load(load_f)

    for pod in load_dict['pod_list']:
        sw = net.addSwitch(pod['name'], protocols=ofversion)
        switch_list.append(sw)
        switch_dict[pod['name']] = sw
        
        for host in pod['host_list']:
            h = net.addHost(host['name'], ip=host['ip'], mac=host['mac'])
            net.addLink(sw, h, 5, bw=3)

    # Add core layer switches
    for i in range(1, pod_num + 1):
        cs_name = f'cs{i}'
        core_switch = net.addSwitch(cs_name, protocols=ofversion)
        for j in range(1, pod_num + 1):
            net.addLink(
                node1 = core_switch,
                node2 = switch_dict[f's{j}'],
                port1 = j,
                port2 = i,
                bw = 1,
            )
        core_switch.start([c1])

    print("***Building network.")
    net.build()
    for sw in switch_list:
        sw.start([c1])
    
    print("***Starting network")
    c1.start()

    print("wait...")
    time.sleep(2)
    # Any host can add all flow tables
    print("***Adding switch rules")
    switch_list[0].cmd('sh ' + switch_rules_file)
    print("***Finished adding switch rules")

    traffic_arr = rt.get_traffic(traffic_file)
    # traffic_arr = traffic_arr[which_row * traffic_num : (which_row + 1) * traffic_num]
    net.simple_CLI(traffic_arr, which_row)

    print("***Stoping network")
    net.stop()


if __name__ == "__main__":
    setLogLevel("info")

    pod_num = rc.pod_num
    which_row = rc.which_row
    traffic_num = rc.a_state_corresponding_traffic_num

    log_path = './log'
    if not os.path.exists(log_path):
        os.makedirs(log_path)

    topology(
        "127.0.0.1",
        "OpenFlow13",
        pod_num,
        which_row,
        traffic_num,
    )
