import sys
import struct
import os
import time

from scapy.all import sniff, sendp, hexdump, get_if_list, get_if_hwaddr
from scapy.all import Packet, IPOption
from scapy.all import ShortField, IntField, LongField, BitField, FieldListField, FieldLenField
from scapy.all import IP, TCP, UDP, Raw, Ether
from scapy.layers.inet import _IPOption_HDR


def handle_pkt(pkt):
    # To avoid receiver duplication
    global DUPLICATION
    if pkt[Ether].src == DUPLICATION:
        # print('DUPLICATION', DUPLICATION)
        # sys.stdout.flush()
        return

    if Raw in pkt:
        raw_load = pkt.sprintf("%Raw.load%") + ',' + str(time.time())
        # or
        # raw_load = pkt[Raw].load.decode()
        print(raw_load)
        sys.stdout.flush()

        # print("got a packet")
        # pkt.show2()
        # print('pkt lenght: ', len(pkt))
        # # hexdump(pkt)
        # sys.stdout.flush()


def main():
    if len(sys.argv) < 1:
        print('pass 1 arguments: <host_name>')
        exit(1)

    # To avoid receiver duplication
    # s1h1, s2h2, ...
    host_name = sys.argv[1]
    global DUPLICATION
    DUPLICATION = '00:00:00:00:00:0' + host_name[1]
    
    sniff(
        filter = 'udp',
        prn = lambda x: handle_pkt(x)
    )


if __name__ == '__main__':
    main()