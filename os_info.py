import platform
import socket
import psutil
import json


hostname = socket.gethostname()
uname = platform.uname()
if_addrs = psutil.net_if_addrs()
for interface_name in if_addrs.items():
    nic_name = interface_name

json_data = [{
    'Hostname': f'{hostname}',
    'System': f'{uname.system}',
    'Nic': f'{nic_name}'
}]
with open(f'{hostname}.json', 'w') as output:
    json.dump(json_data, output)
