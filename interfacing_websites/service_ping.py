import subprocess

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

def ping_host():
    for full_addr in clean_hosts():
        addr = full_addr[0]
        hostname = full_addr[1]
        p = subprocess.Popen(['ping', addr], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        stdout, stderr = p.communicate()
        output = stdout + stderr

        if 'Destination host unreachable.' in output:
            print(f'{hostname}: {addr} is unreachable')
        elif p.returncode != 0:
            print(f'{hostname}: {addr} is down')
        else:
            print(f'{hostname}: {addr} is up')

ping_host()