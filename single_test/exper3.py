# coding=utf-8
from mininet.net import Mininet
from mininet.node import Controller, RemoteController, OVSController
from mininet.node import CPULimitedHost, Host, Node
from mininet.node import OVSKernelSwitch, UserSwitch
from mininet.node import IVSSwitch
from mininet.cli import CLI
from mininet.log import setLogLevel, info
from mininet.link import TCULink, Intf
from subprocess import call
import mininet.util



def myNetwork():
    """
    测试 threshold routing，用meter + group table 分流
               s4 ----
               |      |
        h1 --- s1 --- s2 --- h2
               |      |
               s3 ----
    """

    net = Mininet( topo=None,
                   build=False,
                   ipBase='10.0.0.0/8',
                   switch=UserSwitch,
                   link=TCULink,
                   autoSetMacs=True, autoStaticArp=True)

    info('*** Adding controller\n')
    c0=net.addController(name='c0',
                      controller=RemoteController,
                      ip='127.0.0.1',
                      protocol='tcp',
                      # port=6653)
                      port=6633)

    info('*** Add switches\n')
    s1 = net.addSwitch('s1')
    s2 = net.addSwitch('s2')
    s3 = net.addSwitch('s3')
    s4 = net.addSwitch('s4')

    info('*** Add hosts\n')
    h1 = net.addHost('h1', cls=Host, ip='10.0.0.1', defaultRoute=None)
    h2 = net.addHost('h2', cls=Host, ip='10.0.0.2', defaultRoute=None)

    info('*** Add links\n')
    net.addLink(s1, h1, 1, bw=30)
    net.addLink(s1, s2, 2, 1, bw=10)
    net.addLink(s1, s3, 3, 1, bw=10)
    net.addLink(s3, s2, 2, 3, bw=10)
    net.addLink(s2, h2, 2, bw=30)
    net.addLink(s4, s1, 1, 4, bw=10)
    net.addLink(s4, s2, 2, 4, bw=10)

    info('*** Starting network\n')
    net.build()
    info('*** Starting controllers\n')
    for controller in net.controllers:
        controller.start()

    info('*** Starting switches\n')
    net.get('s1').start([c0])
    net.get('s2').start([c0])
    net.get('s3').start([c0])
    net.get('s4').start([c0])

    info('*** Post configure switches and hosts\n')

    info("Dump all connections in network:\n")
    mininet.util.dumpNetConnections(net)

    # h1.cmd('ethtool -K h1-eth0 tx off')
    # h2.cmd('ethtool -K h2-eth0 tx off')

    CLI(net)
    net.stop()

if __name__ == '__main__':
    setLogLevel( 'info' )
    myNetwork()
