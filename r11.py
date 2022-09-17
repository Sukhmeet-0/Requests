import requests

s=requests.session()
s.verify='path/to/CAs'
# r=requests.get('https://github.com',verify='path/to/CAs')
r=requests.get('https://github.com',verify=False)
