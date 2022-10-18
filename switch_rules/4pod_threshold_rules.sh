dpctl unix:/tmp/s1 meter-mod cmd=add,meter=2 dscp_remark:rate=900,prec_level=1
dpctl unix:/tmp/s1 flow-mod cmd=add,table=0 in_port=1,eth_dst=00:00:00:00:00:02 meter:2 goto:1
dpctl unix:/tmp/s1 flow-mod cmd=add,table=1 in_port=1,eth_type=0x800,eth_dst=00:00:00:00:00:02,ip_dscp=2, apply:output=2,
dpctl unix:/tmp/s1 flow-mod cmd=add,table=1 in_port=1,eth_type=0x800,eth_dst=00:00:00:00:00:02,ip_dscp=0, apply:output=2,
dpctl unix:/tmp/s1 group-mod cmd=add,type=sel,group=2 weight=5, output=3 weight=5, output=4
dpctl unix:/tmp/s1 flow-mod cmd=add,table=1 in_port=1,eth_type=0x800,eth_dst=00:00:00:00:00:02,ip_dscp=4, apply:group=2,
dpctl unix:/tmp/s2 flow-mod cmd=add,table=0 in_port=1,eth_dst=00:00:00:00:00:02, apply:output=2,
dpctl unix:/tmp/s3 flow-mod cmd=add,table=0 in_port=1,eth_dst=00:00:00:00:00:02, apply:output=2,
dpctl unix:/tmp/s2 flow-mod cmd=add,table=0 in_port=3,eth_dst=00:00:00:00:00:02, apply:output=2,
dpctl unix:/tmp/s4 flow-mod cmd=add,table=0 in_port=1,eth_dst=00:00:00:00:00:02, apply:output=2,
dpctl unix:/tmp/s2 flow-mod cmd=add,table=0 in_port=4,eth_dst=00:00:00:00:00:02, apply:output=2,
dpctl unix:/tmp/s1 meter-mod cmd=add,meter=3 dscp_remark:rate=900,prec_level=1
dpctl unix:/tmp/s1 flow-mod cmd=add,table=0 in_port=1,eth_dst=00:00:00:00:00:03 meter:3 goto:1
dpctl unix:/tmp/s1 flow-mod cmd=add,table=1 in_port=1,eth_type=0x800,eth_dst=00:00:00:00:00:03,ip_dscp=2, apply:output=3,
dpctl unix:/tmp/s1 flow-mod cmd=add,table=1 in_port=1,eth_type=0x800,eth_dst=00:00:00:00:00:03,ip_dscp=0, apply:output=3,
dpctl unix:/tmp/s1 group-mod cmd=add,type=sel,group=3 weight=5, output=2 weight=5, output=4
dpctl unix:/tmp/s1 flow-mod cmd=add,table=1 in_port=1,eth_type=0x800,eth_dst=00:00:00:00:00:03,ip_dscp=4, apply:group=3,
dpctl unix:/tmp/s3 flow-mod cmd=add,table=0 in_port=1,eth_dst=00:00:00:00:00:03, apply:output=3,
dpctl unix:/tmp/s2 flow-mod cmd=add,table=0 in_port=1,eth_dst=00:00:00:00:00:03, apply:output=3,
dpctl unix:/tmp/s3 flow-mod cmd=add,table=0 in_port=2,eth_dst=00:00:00:00:00:03, apply:output=3,
dpctl unix:/tmp/s4 flow-mod cmd=add,table=0 in_port=1,eth_dst=00:00:00:00:00:03, apply:output=3,
dpctl unix:/tmp/s3 flow-mod cmd=add,table=0 in_port=4,eth_dst=00:00:00:00:00:03, apply:output=3,
dpctl unix:/tmp/s1 meter-mod cmd=add,meter=4 dscp_remark:rate=900,prec_level=1
dpctl unix:/tmp/s1 flow-mod cmd=add,table=0 in_port=1,eth_dst=00:00:00:00:00:04 meter:4 goto:1
dpctl unix:/tmp/s1 flow-mod cmd=add,table=1 in_port=1,eth_type=0x800,eth_dst=00:00:00:00:00:04,ip_dscp=2, apply:output=4,
dpctl unix:/tmp/s1 flow-mod cmd=add,table=1 in_port=1,eth_type=0x800,eth_dst=00:00:00:00:00:04,ip_dscp=0, apply:output=4,
dpctl unix:/tmp/s1 group-mod cmd=add,type=sel,group=4 weight=5, output=2 weight=5, output=3
dpctl unix:/tmp/s1 flow-mod cmd=add,table=1 in_port=1,eth_type=0x800,eth_dst=00:00:00:00:00:04,ip_dscp=4, apply:group=4,
dpctl unix:/tmp/s4 flow-mod cmd=add,table=0 in_port=1,eth_dst=00:00:00:00:00:04, apply:output=4,
dpctl unix:/tmp/s2 flow-mod cmd=add,table=0 in_port=1,eth_dst=00:00:00:00:00:04, apply:output=4,
dpctl unix:/tmp/s4 flow-mod cmd=add,table=0 in_port=2,eth_dst=00:00:00:00:00:04, apply:output=4,
dpctl unix:/tmp/s3 flow-mod cmd=add,table=0 in_port=1,eth_dst=00:00:00:00:00:04, apply:output=4,
dpctl unix:/tmp/s4 flow-mod cmd=add,table=0 in_port=3,eth_dst=00:00:00:00:00:04, apply:output=4,
dpctl unix:/tmp/s2 meter-mod cmd=add,meter=1 dscp_remark:rate=900,prec_level=1
dpctl unix:/tmp/s2 flow-mod cmd=add,table=0 in_port=2,eth_dst=00:00:00:00:00:01 meter:1 goto:1
dpctl unix:/tmp/s2 flow-mod cmd=add,table=1 in_port=2,eth_type=0x800,eth_dst=00:00:00:00:00:01,ip_dscp=2, apply:output=1,
dpctl unix:/tmp/s2 flow-mod cmd=add,table=1 in_port=2,eth_type=0x800,eth_dst=00:00:00:00:00:01,ip_dscp=0, apply:output=1,
dpctl unix:/tmp/s2 group-mod cmd=add,type=sel,group=1 weight=5, output=3 weight=5, output=4
dpctl unix:/tmp/s2 flow-mod cmd=add,table=1 in_port=2,eth_type=0x800,eth_dst=00:00:00:00:00:01,ip_dscp=4, apply:group=1,
dpctl unix:/tmp/s1 flow-mod cmd=add,table=0 in_port=2,eth_dst=00:00:00:00:00:01, apply:output=1,
dpctl unix:/tmp/s3 flow-mod cmd=add,table=0 in_port=2,eth_dst=00:00:00:00:00:01, apply:output=1,
dpctl unix:/tmp/s1 flow-mod cmd=add,table=0 in_port=3,eth_dst=00:00:00:00:00:01, apply:output=1,
dpctl unix:/tmp/s4 flow-mod cmd=add,table=0 in_port=2,eth_dst=00:00:00:00:00:01, apply:output=1,
dpctl unix:/tmp/s1 flow-mod cmd=add,table=0 in_port=4,eth_dst=00:00:00:00:00:01, apply:output=1,
dpctl unix:/tmp/s2 meter-mod cmd=add,meter=3 dscp_remark:rate=900,prec_level=1
dpctl unix:/tmp/s2 flow-mod cmd=add,table=0 in_port=2,eth_dst=00:00:00:00:00:03 meter:3 goto:1
dpctl unix:/tmp/s2 flow-mod cmd=add,table=1 in_port=2,eth_type=0x800,eth_dst=00:00:00:00:00:03,ip_dscp=2, apply:output=3,
dpctl unix:/tmp/s2 flow-mod cmd=add,table=1 in_port=2,eth_type=0x800,eth_dst=00:00:00:00:00:03,ip_dscp=0, apply:output=3,
dpctl unix:/tmp/s2 group-mod cmd=add,type=sel,group=3 weight=5, output=1 weight=5, output=4
dpctl unix:/tmp/s2 flow-mod cmd=add,table=1 in_port=2,eth_type=0x800,eth_dst=00:00:00:00:00:03,ip_dscp=4, apply:group=3,
dpctl unix:/tmp/s1 flow-mod cmd=add,table=0 in_port=2,eth_dst=00:00:00:00:00:03, apply:output=3,
dpctl unix:/tmp/s3 flow-mod cmd=add,table=0 in_port=1,eth_dst=00:00:00:00:00:03, apply:output=3,
dpctl unix:/tmp/s3 flow-mod cmd=add,table=0 in_port=2,eth_dst=00:00:00:00:00:03, apply:output=3,
dpctl unix:/tmp/s4 flow-mod cmd=add,table=0 in_port=2,eth_dst=00:00:00:00:00:03, apply:output=3,
dpctl unix:/tmp/s3 flow-mod cmd=add,table=0 in_port=4,eth_dst=00:00:00:00:00:03, apply:output=3,
dpctl unix:/tmp/s2 meter-mod cmd=add,meter=4 dscp_remark:rate=900,prec_level=1
dpctl unix:/tmp/s2 flow-mod cmd=add,table=0 in_port=2,eth_dst=00:00:00:00:00:04 meter:4 goto:1
dpctl unix:/tmp/s2 flow-mod cmd=add,table=1 in_port=2,eth_type=0x800,eth_dst=00:00:00:00:00:04,ip_dscp=2, apply:output=4,
dpctl unix:/tmp/s2 flow-mod cmd=add,table=1 in_port=2,eth_type=0x800,eth_dst=00:00:00:00:00:04,ip_dscp=0, apply:output=4,
dpctl unix:/tmp/s2 group-mod cmd=add,type=sel,group=4 weight=5, output=1 weight=5, output=3
dpctl unix:/tmp/s2 flow-mod cmd=add,table=1 in_port=2,eth_type=0x800,eth_dst=00:00:00:00:00:04,ip_dscp=4, apply:group=4,
dpctl unix:/tmp/s1 flow-mod cmd=add,table=0 in_port=2,eth_dst=00:00:00:00:00:04, apply:output=4,
dpctl unix:/tmp/s4 flow-mod cmd=add,table=0 in_port=1,eth_dst=00:00:00:00:00:04, apply:output=4,
dpctl unix:/tmp/s4 flow-mod cmd=add,table=0 in_port=2,eth_dst=00:00:00:00:00:04, apply:output=4,
dpctl unix:/tmp/s3 flow-mod cmd=add,table=0 in_port=2,eth_dst=00:00:00:00:00:04, apply:output=4,
dpctl unix:/tmp/s4 flow-mod cmd=add,table=0 in_port=3,eth_dst=00:00:00:00:00:04, apply:output=4,
dpctl unix:/tmp/s3 meter-mod cmd=add,meter=1 dscp_remark:rate=900,prec_level=1
dpctl unix:/tmp/s3 flow-mod cmd=add,table=0 in_port=3,eth_dst=00:00:00:00:00:01 meter:1 goto:1
dpctl unix:/tmp/s3 flow-mod cmd=add,table=1 in_port=3,eth_type=0x800,eth_dst=00:00:00:00:00:01,ip_dscp=2, apply:output=1,
dpctl unix:/tmp/s3 flow-mod cmd=add,table=1 in_port=3,eth_type=0x800,eth_dst=00:00:00:00:00:01,ip_dscp=0, apply:output=1,
dpctl unix:/tmp/s3 group-mod cmd=add,type=sel,group=1 weight=5, output=2 weight=5, output=4
dpctl unix:/tmp/s3 flow-mod cmd=add,table=1 in_port=3,eth_type=0x800,eth_dst=00:00:00:00:00:01,ip_dscp=4, apply:group=1,
dpctl unix:/tmp/s2 flow-mod cmd=add,table=0 in_port=3,eth_dst=00:00:00:00:00:01, apply:output=1,
dpctl unix:/tmp/s1 flow-mod cmd=add,table=0 in_port=2,eth_dst=00:00:00:00:00:01, apply:output=1,
dpctl unix:/tmp/s1 flow-mod cmd=add,table=0 in_port=3,eth_dst=00:00:00:00:00:01, apply:output=1,
dpctl unix:/tmp/s4 flow-mod cmd=add,table=0 in_port=3,eth_dst=00:00:00:00:00:01, apply:output=1,
dpctl unix:/tmp/s1 flow-mod cmd=add,table=0 in_port=4,eth_dst=00:00:00:00:00:01, apply:output=1,
dpctl unix:/tmp/s3 meter-mod cmd=add,meter=2 dscp_remark:rate=900,prec_level=1
dpctl unix:/tmp/s3 flow-mod cmd=add,table=0 in_port=3,eth_dst=00:00:00:00:00:02 meter:2 goto:1
dpctl unix:/tmp/s3 flow-mod cmd=add,table=1 in_port=3,eth_type=0x800,eth_dst=00:00:00:00:00:02,ip_dscp=2, apply:output=2,
dpctl unix:/tmp/s3 flow-mod cmd=add,table=1 in_port=3,eth_type=0x800,eth_dst=00:00:00:00:00:02,ip_dscp=0, apply:output=2,
dpctl unix:/tmp/s3 group-mod cmd=add,type=sel,group=2 weight=5, output=1 weight=5, output=4
dpctl unix:/tmp/s3 flow-mod cmd=add,table=1 in_port=3,eth_type=0x800,eth_dst=00:00:00:00:00:02,ip_dscp=4, apply:group=2,
dpctl unix:/tmp/s1 flow-mod cmd=add,table=0 in_port=3,eth_dst=00:00:00:00:00:02, apply:output=2,
dpctl unix:/tmp/s2 flow-mod cmd=add,table=0 in_port=1,eth_dst=00:00:00:00:00:02, apply:output=2,
dpctl unix:/tmp/s2 flow-mod cmd=add,table=0 in_port=3,eth_dst=00:00:00:00:00:02, apply:output=2,
dpctl unix:/tmp/s4 flow-mod cmd=add,table=0 in_port=3,eth_dst=00:00:00:00:00:02, apply:output=2,
dpctl unix:/tmp/s2 flow-mod cmd=add,table=0 in_port=4,eth_dst=00:00:00:00:00:02, apply:output=2,
dpctl unix:/tmp/s3 meter-mod cmd=add,meter=4 dscp_remark:rate=900,prec_level=1
dpctl unix:/tmp/s3 flow-mod cmd=add,table=0 in_port=3,eth_dst=00:00:00:00:00:04 meter:4 goto:1
dpctl unix:/tmp/s3 flow-mod cmd=add,table=1 in_port=3,eth_type=0x800,eth_dst=00:00:00:00:00:04,ip_dscp=2, apply:output=4,
dpctl unix:/tmp/s3 flow-mod cmd=add,table=1 in_port=3,eth_type=0x800,eth_dst=00:00:00:00:00:04,ip_dscp=0, apply:output=4,
dpctl unix:/tmp/s3 group-mod cmd=add,type=sel,group=4 weight=5, output=1 weight=5, output=2
dpctl unix:/tmp/s3 flow-mod cmd=add,table=1 in_port=3,eth_type=0x800,eth_dst=00:00:00:00:00:04,ip_dscp=4, apply:group=4,
dpctl unix:/tmp/s1 flow-mod cmd=add,table=0 in_port=3,eth_dst=00:00:00:00:00:04, apply:output=4,
dpctl unix:/tmp/s4 flow-mod cmd=add,table=0 in_port=1,eth_dst=00:00:00:00:00:04, apply:output=4,
dpctl unix:/tmp/s2 flow-mod cmd=add,table=0 in_port=3,eth_dst=00:00:00:00:00:04, apply:output=4,
dpctl unix:/tmp/s4 flow-mod cmd=add,table=0 in_port=2,eth_dst=00:00:00:00:00:04, apply:output=4,
dpctl unix:/tmp/s4 flow-mod cmd=add,table=0 in_port=3,eth_dst=00:00:00:00:00:04, apply:output=4,
dpctl unix:/tmp/s4 meter-mod cmd=add,meter=1 dscp_remark:rate=900,prec_level=1
dpctl unix:/tmp/s4 flow-mod cmd=add,table=0 in_port=4,eth_dst=00:00:00:00:00:01 meter:1 goto:1
dpctl unix:/tmp/s4 flow-mod cmd=add,table=1 in_port=4,eth_type=0x800,eth_dst=00:00:00:00:00:01,ip_dscp=2, apply:output=1,
dpctl unix:/tmp/s4 flow-mod cmd=add,table=1 in_port=4,eth_type=0x800,eth_dst=00:00:00:00:00:01,ip_dscp=0, apply:output=1,
dpctl unix:/tmp/s4 group-mod cmd=add,type=sel,group=1 weight=5, output=2 weight=5, output=3
dpctl unix:/tmp/s4 flow-mod cmd=add,table=1 in_port=4,eth_type=0x800,eth_dst=00:00:00:00:00:01,ip_dscp=4, apply:group=1,
dpctl unix:/tmp/s2 flow-mod cmd=add,table=0 in_port=4,eth_dst=00:00:00:00:00:01, apply:output=1,
dpctl unix:/tmp/s1 flow-mod cmd=add,table=0 in_port=2,eth_dst=00:00:00:00:00:01, apply:output=1,
dpctl unix:/tmp/s3 flow-mod cmd=add,table=0 in_port=4,eth_dst=00:00:00:00:00:01, apply:output=1,
dpctl unix:/tmp/s1 flow-mod cmd=add,table=0 in_port=3,eth_dst=00:00:00:00:00:01, apply:output=1,
dpctl unix:/tmp/s1 flow-mod cmd=add,table=0 in_port=4,eth_dst=00:00:00:00:00:01, apply:output=1,
dpctl unix:/tmp/s4 meter-mod cmd=add,meter=2 dscp_remark:rate=900,prec_level=1
dpctl unix:/tmp/s4 flow-mod cmd=add,table=0 in_port=4,eth_dst=00:00:00:00:00:02 meter:2 goto:1
dpctl unix:/tmp/s4 flow-mod cmd=add,table=1 in_port=4,eth_type=0x800,eth_dst=00:00:00:00:00:02,ip_dscp=2, apply:output=2,
dpctl unix:/tmp/s4 flow-mod cmd=add,table=1 in_port=4,eth_type=0x800,eth_dst=00:00:00:00:00:02,ip_dscp=0, apply:output=2,
dpctl unix:/tmp/s4 group-mod cmd=add,type=sel,group=2 weight=5, output=1 weight=5, output=3
dpctl unix:/tmp/s4 flow-mod cmd=add,table=1 in_port=4,eth_type=0x800,eth_dst=00:00:00:00:00:02,ip_dscp=4, apply:group=2,
dpctl unix:/tmp/s1 flow-mod cmd=add,table=0 in_port=4,eth_dst=00:00:00:00:00:02, apply:output=2,
dpctl unix:/tmp/s2 flow-mod cmd=add,table=0 in_port=1,eth_dst=00:00:00:00:00:02, apply:output=2,
dpctl unix:/tmp/s3 flow-mod cmd=add,table=0 in_port=4,eth_dst=00:00:00:00:00:02, apply:output=2,
dpctl unix:/tmp/s2 flow-mod cmd=add,table=0 in_port=3,eth_dst=00:00:00:00:00:02, apply:output=2,
dpctl unix:/tmp/s2 flow-mod cmd=add,table=0 in_port=4,eth_dst=00:00:00:00:00:02, apply:output=2,
dpctl unix:/tmp/s4 meter-mod cmd=add,meter=3 dscp_remark:rate=900,prec_level=1
dpctl unix:/tmp/s4 flow-mod cmd=add,table=0 in_port=4,eth_dst=00:00:00:00:00:03 meter:3 goto:1
dpctl unix:/tmp/s4 flow-mod cmd=add,table=1 in_port=4,eth_type=0x800,eth_dst=00:00:00:00:00:03,ip_dscp=2, apply:output=3,
dpctl unix:/tmp/s4 flow-mod cmd=add,table=1 in_port=4,eth_type=0x800,eth_dst=00:00:00:00:00:03,ip_dscp=0, apply:output=3,
dpctl unix:/tmp/s4 group-mod cmd=add,type=sel,group=3 weight=5, output=1 weight=5, output=2
dpctl unix:/tmp/s4 flow-mod cmd=add,table=1 in_port=4,eth_type=0x800,eth_dst=00:00:00:00:00:03,ip_dscp=4, apply:group=3,
dpctl unix:/tmp/s1 flow-mod cmd=add,table=0 in_port=4,eth_dst=00:00:00:00:00:03, apply:output=3,
dpctl unix:/tmp/s3 flow-mod cmd=add,table=0 in_port=1,eth_dst=00:00:00:00:00:03, apply:output=3,
dpctl unix:/tmp/s2 flow-mod cmd=add,table=0 in_port=4,eth_dst=00:00:00:00:00:03, apply:output=3,
dpctl unix:/tmp/s3 flow-mod cmd=add,table=0 in_port=2,eth_dst=00:00:00:00:00:03, apply:output=3,
dpctl unix:/tmp/s3 flow-mod cmd=add,table=0 in_port=4,eth_dst=00:00:00:00:00:03, apply:output=3,
