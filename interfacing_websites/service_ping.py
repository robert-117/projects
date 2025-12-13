import subprocess
import os
from subprocess import DEVNULL
from sys import stdout


# print(os.getcwd())
# res = subprocess.run(['wsl', '-d', 'Ubuntu-20.04', 'ls', '-l', '/home/rcarpenter/code_proj/projects/interfacing_websites'], \
#                check=True, text=True, capture_output=True)
# print(res.stdout)
# print(res.stderr)

def clean_hosts(host_file='test-hosts'):
    with open(host_file, 'r') as f:
        host_list = []
        for line in f:
            hostname = line.split()[0:]
            if not hostname or '#' in hostname:
                continue
            else:
                host_list.append(hostname)
        return host_list

for full_addr in clean_hosts():
    addr = full_addr[0]
    hostname = full_addr[1]
    p = subprocess.Popen(f'ping {addr}', shell=False, stdout=DEVNULL)
    p.wait()
    if p.poll():
        print(addr+" is down")
        print(p.stdout)
    # TODO need to account for destination unreachable
    # elif 'Destination host unreachable.' in p.stdout.decode('utf-8'):
    #     print (addr+" is unreachable")
    else:
        print(addr+" is up")
        print(p.stdout)

def ping_host(host):
    ping_result = subprocess.check_output(['ping', '-c', '1', '-W', host])
    print(ping_result)







