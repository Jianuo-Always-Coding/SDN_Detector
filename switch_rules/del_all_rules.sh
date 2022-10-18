#!/usr/bin/env bash
# flow和table表都能不指定id，代表全删，并成功。
# meter表这样执行后，虽然返回OK，但其实meter表每项配置没被删除。
# 那只能单条删除了，执行多次。

POD_NUM=4

function del_rules(){
    switch=$1
    type=$2

    if [ $type == "meter-mod" ]; then
        for((i=1;i<=${POD_NUM};i++)); do
            echo "dpctl unix:/tmp/s${switch} ${type} cmd=del,meter=$i"
            dpctl unix:/tmp/s${switch} ${type} cmd=del,meter=$i
        done
    else
        echo "dpctl unix:/tmp/s${switch} ${type} cmd=del"
        dpctl unix:/tmp/s${switch} ${type} cmd=del
    fi
}

for k in $(seq ${POD_NUM})
do
    del_rules $k flow-mod
    del_rules $k group-mod
    del_rules $k meter-mod
done