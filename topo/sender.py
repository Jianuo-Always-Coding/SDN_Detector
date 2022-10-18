import argparse
import sys
import socket
import random
import struct
import time
import math

from scapy.all import sendp, send, sendpfast, get_if_list, get_if_hwaddr
from scapy.all import Packet
from scapy.all import Ether, IP, UDP, TCP


def main():

    if len(sys.argv) < 3:
        print('pass 2 arguments: <dst_ip> <dst_mac> <flag>')
        exit(1)

    addr = socket.gethostbyname(sys.argv[1])
    mac = sys.argv[2]
    # MTU = 1500 byte
    # The length of message should be less than or equal to 1472 byte
    # message pattern: <timestamp>,<src_ip>,<dst_ip>,<flag>,<filler>
    flag = sys.argv[3]
    rate_kbps = int(sys.argv[4])
    traffic_line = sys.argv[5]

    pkt =  Ether(dst=mac)
    pkt = pkt / IP(dst=addr, tos=0x8) / UDP(dport=1234, sport=random.randint(49152,65535))
    
    src_ip = pkt.sprintf("%IP.src%")
    dst_ip = pkt.sprintf("%IP.dst%")

    
    # TODO: simulate different traffic rate
    # NOTICE: packet_count
    packet_count = int(flag)
    if packet_count == 0:
        return

    pkt_list = []
    for i in range(packet_count):
        message = str(time.time()) + ',' + src_ip + ',' + dst_ip + ',' + str(i) + ',' + traffic_line +','
        message = message.ljust(1472, 'f')
        # message = message.ljust(100, 'f')
        tmp_pkt = pkt / message
        # the length of tmp_pkt is just 1024 byte = 1KB
        pkt_list.append(tmp_pkt)

    # Calculates packet per second
    packet_size_kbit = 8 * 1500 / 1024
    packet_per_sec = int(rate_kbps / packet_size_kbit)
    window = max(8, int(packet_per_sec / 10))
    window_ub = packet_per_sec * 2
    start = 0
    start_time = time.time()
    while start < packet_count:
        end_index = start + window
        if end_index > packet_count:
            end_index = packet_count
        sendpfast(pkt_list[start : end_index], pps = packet_per_sec, replay_args = ['--pps-multi='+str(window)])
        start = start + window
        expected_finish_time = start * packet_size_kbit / rate_kbps
        actual_finish_time = time.time() - start_time

        if actual_finish_time < expected_finish_time:
            time.sleep(expected_finish_time - actual_finish_time)
            if actual_finish_time < expected_finish_time - 0.1:
                window = math.ceil(window * 0.8)
        else:
            window = min(window * 2, window_ub)

        # completion time probe, flag -1 as traffic_line
        probe = str(time.time()) + ',' + src_ip + ',' + dst_ip + ',' + str(i) + ',-1,' + 'probe'
        pkt_probe = pkt / probe
        sendp(pkt_probe)

    duration = actual_finish_time
    # mpbs: MBits per second
    # sendpfast(pkt_list, mbps = packet_count / 1024)
    print(src_ip, '->',dst_ip, ', ', packet_count, 'time-consuming: ',duration, 'expected sending rate(kbps): ', rate_kbps, 'actual sending rate(kbps): ', packet_count * packet_size_kbit / duration, 'window size: ', window)
    # pkt_list[0].show2()
    

if __name__ == '__main__':
    main()