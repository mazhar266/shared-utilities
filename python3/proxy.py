import requests

config = {
    'http': 'http://mazhar:slowkoala72@roaster.iammaze.com:4632',
    'https': 'http://mazhar:slowkoala72@roaster.iammaze.com:4632',
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
