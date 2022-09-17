import requests

s=requests.Session()
userName={'username':'john99'}
location={'location':'india'}

setCookieUrl="https://httpbin.org/cookies/set"
getCookieUrl='https://httpbin.org/cookies'

s.get(setCookieUrl,params=userName)
s.get(setCookieUrl,params=location)

r=s.get(getCookieUrl)
print(r.text)