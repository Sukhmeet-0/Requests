import  requests

# r=requests.get("https://api.github.com/events")
# # events=r.json()
# # # print(events[0])
# # print(events[1]['id'])

data={'firstName':'Sukhmeet','lastName':'singh'}
r=requests.post('https://httpbin.org/post',json=data)
print(r.text)