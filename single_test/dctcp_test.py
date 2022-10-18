from mininet.net import Mininet
from mininet.node import Controller, RemoteController, OVSController
from mininet.node import CPULimitedHost, Host, Node
from mininet.node import OVSKernelSwitch, UserSwitch
from mininet.node import IVSSwitch
from mininet.cli import CLI
from mininet.log import setLogLevel, info
from mininet.link import TCLink, Intf
from subprocess import call
import mininet.util


def myNetwork():
    """
        h1 --- s1 --- s2 --- h2
               |      |
               s3 ----
    """

    net = Mininet( topo=None,
                   build=False,
                   ipBase='10.0.0.0/8',
                   switch=OVSKernelSwitch,
                   autoSetMacs=True, autoStaticArp=True)

    info('*** Adding controller\n')
    c0=net.addController(name='c0',
                      controller=RemoteController,
                      ip='127.0.0.1',
                      protocol='tcp',
                      # port=6653)
                      port=6633)

    info('*** Add switches\n')
    s3 = net.addSwitch('s3')
    s1 = net.addSwitch('s1')
    s2 = net.addSwitch('s2')

    info('*** Add hosts\n')
    h2 = net.addHost('h2', cls=Host, ip='10.0.0.2', defaultRoute=None)
    h1 = net.addHost('h1', cls=Host, ip='10.0.0.1', defaultRoute=None)

    info('*** Add links\n')
    net.addLink(s1, h1)
    net.addLink(s1, s2)
    net.addLink(s1, s3)
    net.addLink(s3, s2)
    net.addLink(s2, h2)
    # net.addLink(s1, h1, enable_ecn=True)
    # net.addLink(s1, s2, enable_ecn=True)
    # net.addLink(s1, s3, enable_ecn=True)
    # net.addLink(s3, s2, enable_ecn=True)
    # net.addLink(s2, h2, enable_ecn=True)

    info('*** Starting network\n')
    net.build()
    info('*** Starting controllers\n')
    for controller in net.controllers:
        controller.start()

    info('*** Starting switches\n')
    net.get('s1').start([c0])
    net.get('s2').start([c0])
    net.get('s3').start([c0])

    info('*** Post configure switches and hosts\n')

    info("Dump all connections in network:\n")
    mininet.util.dumpNetConnections(net)

    CLI(net)
    net.stop()

if __name__ == '__main__':
    setLogLevel( 'info' )
    myNetwork()
