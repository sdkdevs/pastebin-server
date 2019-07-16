import requests
import json
import os

payload = {
    'title': "title",
    'lang': "rust",
    'content': "// content",
    'expiration': 3600
}

json.dump(payload,open('post.txt','w'))
url = "http://localhost:8088/record"

resp = requests.post(url,json=payload)
print(resp.status_code)
print(resp.json())

input()

bench = f'ab -n 100000 -c 100 -p post.txt  -T "application/json" {url}'
print(bench)
os.system(bench)
os.system('tail server.log')
