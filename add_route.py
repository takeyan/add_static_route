import yaml
import json

routes = ""
gateway = ""
dest_cidr = "172.18.0.0/18"

with open(r'50-cloud-init.yaml.backup') as file:
    netplan = yaml.load(file, Loader=yaml.FullLoader)
    routes = netplan['network']['ethernets']['eth0']['routes']

for route in routes:
    if route['to'] == '10.0.0.0/8':
        gateway = route['via']

newroute = f'{{ \"to\" : \"{dest_cidr}\" , \"via\" : \"{gateway}\" }}'
netplan['network']['ethernets']['eth0']['routes'].append(json.loads(newroute))

with open(r'50-cloud-init-test.yaml', 'w') as file:
    res = yaml.dump(netplan, file)


