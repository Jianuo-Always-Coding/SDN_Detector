dpctl unix:/tmp/s1 meter-mod cmd=add,meter=2 dscp_remark:rate=8500,prec_level=1
dpctl unix:/tmp/s1 flow-mod cmd=add,table=0 in_port=1,eth_type=0x800,eth_dst=00:00:00:00:00:02,ip_dscp=2 meter:2 goto:1
dpctl unix:/tmp/s1 flow-mod cmd=add,table=0 in_port=1,eth_type=0x800,eth_dst=00:00:00:00:00:02,ip_dscp=0 apply:output=2
dpctl unix:/tmp/s1 flow-mod cmd=add,table=1 in_port=1,eth_type=0x800,eth_dst=00:00:00:00:00:02,ip_dscp=2 apply:output=2

dpctl unix:/tmp/s1 group-mod cmd=add,type=sel,group=2 weight=5, output=3 weight=5, output=4
dpctl unix:/tmp/s1 flow-mod cmd=add,table=1 in_port=1,eth_type=0x800,eth_dst=00:00:00:00:00:02,ip_dscp=4 apply:group=2

dpctl unix:/tmp/s3 flow-mod cmd=add,table=0 in_port=1,eth_dst=00:00:00:00:00:02, apply:output=2
dpctl unix:/tmp/s4 flow-mod cmd=add,table=0 in_port=1,eth_dst=00:00:00:00:00:02, apply:output=2
dpctl unix:/tmp/s2 flow-mod cmd=add,table=0 in_port=3,eth_dst=00:00:00:00:00:02, apply:output=2
dpctl unix:/tmp/s2 flow-mod cmd=add,table=0 in_port=1,eth_dst=00:00:00:00:00:02, apply:output=2
dpctl unix:/tmp/s2 flow-mod cmd=add,table=0 in_port=4,eth_dst=00:00:00:00:00:02, apply:output=2

dpctl unix:/tmp/s2 meter-mod cmd=add,meter=1 dscp_remark:rate=8500,prec_level=1
dpctl unix:/tmp/s2 flow-mod cmd=add,table=0 in_port=2,eth_type=0x800,eth_dst=00:00:00:00:00:01,ip_dscp=2 meter:1 goto:1
dpctl unix:/tmp/s2 flow-mod cmd=add,table=0 in_port=2,eth_type=0x800,eth_dst=00:00:00:00:00:01,ip_dscp=0 apply:output=1
dpctl unix:/tmp/s2 flow-mod cmd=add,table=1 in_port=2,eth_type=0x800,eth_dst=00:00:00:00:00:01,ip_dscp=2 apply:output=1

dpctl unix:/tmp/s2 group-mod cmd=add,type=sel,group=1 weight=5, output=3 weight=5, output=4
dpctl unix:/tmp/s2 flow-mod cmd=add,table=1 in_port=3,eth_type=0x800,eth_dst=00:00:00:00:00:01,ip_dscp=4 apply:group=1

dpctl unix:/tmp/s3 flow-mod cmd=add,table=0 in_port=2,eth_dst=00:00:00:00:00:01, apply:output=1
dpctl unix:/tmp/s4 flow-mod cmd=add,table=0 in_port=2,eth_dst=00:00:00:00:00:01, apply:output=1
dpctl unix:/tmp/s1 flow-mod cmd=add,table=0 in_port=3,eth_dst=00:00:00:00:00:01, apply:output=1
dpctl unix:/tmp/s1 flow-mod cmd=add,table=0 in_port=2,eth_dst=00:00:00:00:00:01, apply:output=1
dpctl unix:/tmp/s1 flow-mod cmd=add,table=0 in_port=4,eth_dst=00:00:00:00:00:01, apply:output=1