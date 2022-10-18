# DONE
测试 threshold-routing 中 clos topo加打流ok，连续打流调用的是封装好的iperf，另外还有写好的 scapy 打流，可以写论文用。

从threshold-routing工程移植必要模块。

构建 clos 拓扑。
# TODO

流量检测启动ryu控制器，用restapi采集流量。 可以与iperf的log对比/结合。

流量读取和记录均用csv。

算法借鉴 sliding window change detection 论文，博客，或者用一些统计量。

仿真架构规划，可拓展性方面也可以写。


# Guide

## Install
Ubuntu 18.04

```
sudo apt install python3-pip

sudo apt install git

git clone git://github.com/mininet/mininet

cd mininet/util
vim install.sh
修改python为python3
PYTHON=${PYTHON:-python3}

./install.sh -n3fwmv    命令会含ofsoftswitch13一起安装

单独装ryu，省得报错
git clone git://github.com/osrg/ryu.git
cd ryu
sudo python3 setup.py install


pip3 install numpy
```

（若如上单独安装了ryu这里可忽略）若想直接用 ./install.sh -nfwv3y 需要在执行前修改 install.sh
```
--- a/util/install.sh
+++ b/util/install.sh
@@ -103,7 +103,7 @@ function version_ge {
 }

 # Attempt to detect Python version
-PYTHON=${PYTHON:-python}
+PYTHON=${PYTHON:-python3}
 PRINTVERSION='import sys; print(sys.version_info)'
 PYTHON_VERSION=unknown
 for python in $PYTHON python2 python3; do
@@ -487,7 +487,8 @@ function ryu {

     # fetch RYU
     cd $BUILD_DIR/
-    git clone git://github.com/osrg/ryu.git ryu
+    # caopeirui annotate
+    #git clone git://github.com/osrg/ryu.git ryu
     cd ryu

     # install ryu
@@ -496,7 +497,8 @@ function ryu {
     sudo python setup.py install

     # Add symbolic link to /usr/bin
-    sudo ln -s ./bin/ryu-manager /usr/local/bin/ryu-manager
+    # caopeirui annotate
+    #sudo ln -s ./bin/ryu-manager /usr/local/bin/ryu-manager
 }
```

## Run
```
cd topo

sudo python3 create_clos_topo.py

等待出现
please input custom control cmd:
e: exit t: traffic c: cli r: recv s: send

输入 t 即可实现打流

打流日志见 topo/log/
```

### ryu 控制器 rest api server
```
cd ryu_rest_api
ryu-manager ofctl_rest.py
```
封装好的 rest api 见 `ryu_rest_api/request_ryu.py`

### debug ryu
启动ryu控制器后，若出现缺少某个包，直接用 pip3 install 安装之。

若出现 `unsupported version 0x1”. If possible, set the switch to use one of the versions [4]`， 重新安装 ofsoftswitch13
```
cd ofsoftswitch13
./boot.sh
./configure
make
sudo make install
```
- https://blog.csdn.net/guizaijianchic/article/details/77951780
- https://blog.csdn.net/jmh1996/article/details/72670617

# SDN_Detector
# SDN_Detector
