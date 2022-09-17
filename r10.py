import requests

# proxies={'https://httpbin.org':'198.211.101.99:3128'}
proxies={'http':'198.211.101.99:3128'}
r =requests.get('https://httpbin.org/ip',proxies=proxies)
print(r.text)