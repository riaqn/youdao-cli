#!/bin/env python
keyfrom = 'jvhuatk'
key = 1230989153
from sys import argv
query = ' '.join(argv[1:])

from urllib.request import urlopen
from urllib.parse import quote
res = urlopen('http://fanyi.youdao.com/openapi.do?keyfrom=%s&key=%d&type=data&doctype=json&version=1.1&q=' % (keyfrom, key) + quote(query))

from json import loads
result = loads(res.read().decode('utf-8'))
print(', '.join(result['translation']))
print()

try:
    print(result['query'], '[%s]' % (result['basic']['phonetic']))
except KeyError:
    print(result['query'])
    
for explain in result['basic']['explains']:
    print(explain)

print()
for explain in result['web']:
    print(explain['key'], ','.join(explain['value']))
