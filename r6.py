import requests

# r=requests.get('https://httpbin.org/status/404')
# r.raise_for_status()
r=requests.get('https://httpbin.org/status/200',timeout=0.1)
r.raise_for_status()