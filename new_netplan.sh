#!/bin/bash
cd /tmp
cidr = "172.18.0.0/18"
git clone https://github.com/takeyan/add_static_route.git
cd add_static_route
files="/etc/netplan/*.yaml"
for file in $files; do
    mv $file ${file}.backup
    python3 add_route.py ${file}.backup $cidr
    break
done
netplan apply

