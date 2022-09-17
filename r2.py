import requests

url="https://httpbin.org/post"
files = {'file': open(r'C:\Users\sukhm\Desktop\Requests\sample.csv','rb')}
r = requests.post(url, files=files)
print(r.status_code)
print(r.text)