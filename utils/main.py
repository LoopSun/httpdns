# -*- coding: utf-8 -*-

import os

from utils.ipip import IP
from utils.ipip import IPX

IP_DATA_FILE = os.path.abspath(os.path.join("resource","17monipdb.dat"))

IP.load(IP_DATA_FILE)
print(IP.find("27.47.129.52"))
print(IP.find("202.66.30.182"))
print(IP.find("193.54.67.1"))

acl_list = [
    ("1.1.1.1", ["广州"]),
    ("8.8.8.8", ["美国"]),
]
