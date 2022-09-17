import requests as r
headers={'content-type':'multipart/form-data'}
rr=r.post('https://httpbin.org/post',headers=headers)
# print(rr.request.headers,end="\n")
print(rr.headers['content-type'])