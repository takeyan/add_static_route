#!/bin/bash
git clone https://github.com/takeyan/add_static_route.git
cd add_static_route
pip install pyyaml
mv /etc/netplan/50-cloud-init.yaml /etc/netplan/50-cloud-init.yaml.backup
python3 add_route.py  
netplan apply
