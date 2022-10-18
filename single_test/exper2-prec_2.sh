dpctl unix:/tmp/s1 meter-mod cmd=add,meter=1 dscp_remark:rate=8000,prec_level=2
dpctl unix:/tmp/s1 flow-mod cmd=add,table=0 in_port=1 meter:1 goto:1
dpctl unix:/tmp/s1 flow-mod cmd=add,table=1 in_port=1,eth_type=0x800,ip_dscp=2 apply:output=2
dpctl unix:/tmp/s1 flow-mod cmd=add,table=1 in_port=1,eth_type=0x800,ip_dscp=6 apply:output=3
dpctl unix:/tmp/s3 flow-mod cmd=add,table=0 in_port=1, apply:output=2
dpctl unix:/tmp/s2 flow-mod cmd=add,table=0 in_port=2, apply:output=3
dpctl unix:/tmp/s2 flow-mod cmd=add,table=0 in_port=1, apply:output=3

dpctl unix:/tmp/s2 meter-mod cmd=add,meter=1 dscp_remark:rate=8000,prec_level=2
dpctl unix:/tmp/s2 flow-mod cmd=add,table=0 in_port=3 meter:1 goto:1
dpctl unix:/tmp/s2 flow-mod cmd=add,table=1 in_port=3,eth_type=0x800,ip_dscp=2 apply:output=1
dpctl unix:/tmp/s2 flow-mod cmd=add,table=1 in_port=3,eth_type=0x800,ip_dscp=6 apply:output=2
dpctl unix:/tmp/s3 flow-mod cmd=add,table=0 in_port=2, apply:output=1
dpctl unix:/tmp/s1 flow-mod cmd=add,table=0 in_port=3, apply:output=1
dpctl unix:/tmp/s1 flow-mod cmd=add,table=0 in_port=2, apply:output=1
