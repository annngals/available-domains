# -*- coding: utf-8 -*-
"""
Created on Wed Oct 21 14:45:58 2020

@author: Anna Galsanova
"""

import json
import re
import whois
import sys
from urllib.parse import urlparse

with open("json.json", "r") as read_file:
    data = json.load(read_file)

https = []

for p in data['2020-10-20']:
    match = re.search('https', p['link'])
    if (match):
        https.append(p['link'])
        
print (https)
        
domains = []

for url in https:
    parse = urlparse(url)
    if 'www' in url:
        a = 1
    else:
        a = 0
    domain = parse.netloc.split(".")[a:]
    host = ".".join(domain)
    domains.append(host)
    
print (domains)

for page in domains:
    try:
        whois.whois(page)
        sys.stderr.flush()
    except Exception:
        print('available domain: %s' % (page))