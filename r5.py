import requests as r
import requests.cookies

url='https://httpbin.org/cookies'
cookies={'location': 'New York'}
# rr=r.get(url,cookies=cookies)
# print(rr.text)

# r2=r.get('https://google.com')
# print(r2.cookies['IP_JAR'])

requestJar=requests.cookies.RequestsCookieJar()
requestJar.set("userId","John99",domain="httpbin.org",path='/cookies')
requestJar.set("cartItem","Laptop",domain="httpbin.org",path='/cookies')

r3=requests.get(url,cookies=requestJar)
print(r3.text)
