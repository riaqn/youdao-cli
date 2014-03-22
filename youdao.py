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

bold='\033[1m'
cyan='\033[0;36m'
highlight = '\033[1;31m'
end = '\033[0m'

from re import sub, IGNORECASE

try:
    print('%s%s%s' % (bold, result['query'], end), '%s[%s]%s' % (cyan, result['basic']['phonetic'], end))
except KeyError:
    print(result['query'])
    
for explain in result['basic']['explains']:
    print(sub(r'^([a-z]+\.)', r'%s\1%s' % (bold, end), explain))


print()
for explain in result['web']:
    print(sub(r'(\b)(%s)(\b)' % (result['query'],), r'\1%s\2%s\3' % (highlight, end), explain['key'], flags=IGNORECASE), ','.join(explain['value']))
