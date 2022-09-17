import requests

payload ={"FirstName":"Sukhmeet","LastName":"Singh"}
# r=requests.get("https://httpbin.org/get",params=payload)
r=requests.post("https://httpbin.org/post",data=payload)
# print(r.status_code)
# print(r.url)
print(r.text)
