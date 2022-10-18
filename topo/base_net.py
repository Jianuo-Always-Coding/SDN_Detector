from mininet.net import Mininet
import time
import random
import sched
from mininet.cli import CLI


class BaseNet(Mininet):
    def simple_CLI(self, traffic_arr, which_row):
        while(True):
            print('please input custom control cmd:\ne: exit t: traffic c: cli ')
            cmd = input()
            if cmd in {'e', 'exit'}:
                break
            elif cmd in {'t', 'traffic'}:
                # Every element in time_arr represents a flow duration.
                time_arr = [5 for i in range(len(traffic_arr))]
                self.simulate_traffic(traffic_arr, time_arr)
            elif cmd in {'c', 'cli'}:
                CLI(self)
           


    def iperf_single(self, hosts = None, bw = '1M', period = 1, port = 5001, verbose=False):
        if not hosts or len(hosts) != 2:
            return
        client, server = hosts
        servername = server.name
        clientname = client.name

        server_command = 'iperf -u -s -p ' + str(port) +' -i 1 >> log/'
        client_command = 'iperf -u -t ' + str(period) + ' -c ' + server.IP() + ' -b ' + bw + ' -p ' + str(port) +' --tos 0x08 >> log/'
        server_command += clientname + 'B' + servername +' &'
        client_command += clientname +'T' + servername +' &'

        server.cmd(server_command)
        ret = client.cmd(client_command)
        print(clientname + '->' + servername + ' bw: ' + bw + ' port ' + str(port))
        print(server_command)
        print(client_command)
        print(ret)

        if not verbose:
            return
        print(clientname + '->' + servername)
        print(server_command)
        print(client_command)
        # iperf -t 10 -c 10.0.0.2 -b 10M > client&


    def simulate_traffic(self, traffic_arr, time_arr, log=False):
        if(len(traffic_arr) != len(time_arr)):
            print('input data error: traffic and data no match')
            return
        length = len(traffic_arr)
        timing = 0
        host_list = [h for h in self.hosts]
        host_num = len(host_list)
        # schedule = sched.scheduler(time.time,time.sleep)
        port = 5001
        for n in range(length):
            for i in range(host_num):
                for j in range(host_num):
                    if(i != j):
                        flow_duration = time_arr[n]
                        flow = float(traffic_arr[n][i][j])

                        if flow > 0.0:
                            # schedule.enter(timing, 1, self.iperf_single, ([host_list[i], host_list[j]], str(flow) + 'K', flow_duration, port, log))
                            self.iperf_single([host_list[i], host_list[j]], str(flow) + 'K', flow_duration, port, log)
                            port += random.randint(1, host_num)
                            time.sleep(.05)
            timing += time_arr[n]
        # schedule.run()
    
    
    def recv(self):
        host_list = [h for h in self.hosts]
        # TODO: Existed detection
        for i in range(len(host_list)):
            ret = host_list[i].cmd('python3 receiver.py ' + str(host_list[i]) + ' >> log/recv' + str(i + 1) + '.log &')
            print(str(i + 1) + 'recv() status: ', ret)


    def send(self, traffic_arr, which_row):
        host_list = [h for h in self.hosts]
        # host_list[1].cmd('python3 sender.py 10.0.1.1 00:00:00:00:00:01 10 >> log/send.log &')
        # return
        host_num = len(host_list)
        length = len(traffic_arr)
        for n in range(length):
            traffic_line = which_row * length + n
            print('The ' + str(traffic_line) + 'th line of traffic file:')
            for i in range(host_num):
                for j in range(host_num):
                    if(i != j):
                        rate_kbps = int(traffic_arr[n][i][j])
                        if rate_kbps > 0:
                            # NOTICE: 4, packet_count
                            # packet_count is 4 times as much as rate_kbps just to make latter flows more stable
                            packet_count = rate_kbps * 4
                            send_cmd_str = ('python3 sender.py 10.0.' + str(j + 1)
                                + '.1 00:00:00:00:00:0' + str(j + 1)
                                + ' ' + str(packet_count)
                                + ' ' + str(rate_kbps)
                                + ' ' + str(traffic_line) + ' >> log/send.log &')
                            host_list[i].cmd(send_cmd_str)
                            print(send_cmd_str)
            
            print('wait the traffic to send...')
            # detect whether sending finished
            start_time = time.time()
            end_time = 0
            while True:
                ret = host_list[0].cmd('ps axu | grep sender.py')
                if 'python3 sender.py' not in ret:
                    print('finish!')
                    end_time = time.time()
                    break
                time.sleep(1)
            print('time-consuming:', end_time - start_time)







