import yaml
import json
import sys

args = sys.argv

routes = ""
gateway = ""
netp_yaml = args[1]
netp_bkup = f'{netp_yaml}.backup'
dest_cidr = args[2]

with open(netp_bkup) as file:
    netplan = yaml.load(file)
    routes = netplan['network']['ethernets']['eth0']['routes']

for route in routes:
    if route['to'] == '10.0.0.0/8':
        gateway = route['via']

newroute = f'{{ \"to\" : \"{dest_cidr}\" , \"via\" : \"{gateway}\" }}'
netplan['network']['ethernets']['eth0']['routes'].append(json.loads(newroute))

with open(netp_yaml, 'w') as file:
    file.write(yaml.dump(netplan, default_flow_style=False))

