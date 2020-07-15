import json
import requests

print("Requesting webshare for proxies")
response = requests.get(
    "https://proxy.webshare.io/api/proxy/list/?page=1",
    headers={"Authorization": "Token {}".format('WEBSHARE_TOKEN')}
)
proxies = response.json()
print("Got {} proxies".format(proxies['count']))

i = 1
for proxy in proxies['results']:
    print('Proxy: {}'.format(i))
    config = {
        'http': 'http://{}:{}@{}:{}'.format(
            proxy['username'],
            proxy['password'],
            proxy['proxy_address'],
            proxy['ports']['http']
        ),
        'https': 'http://{}:{}@{}:{}'.format(
            proxy['username'],
            proxy['password'],
            proxy['proxy_address'],
            proxy['ports']['http']
        ),
    }
    ip = requests.get('http://api.ipify.org', proxies=config).text
    print('IP: {}'.format(ip))
    location = requests.get(
        'http://ip-api.com/json/{}'.format(ip),
        proxies=config
    ).json()
    print('Location: {}, {}, {}'.format(
        location['city'],
        location['regionName'],
        location['country']
    ))
    i = i + 1
