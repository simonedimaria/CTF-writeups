---
Category: WEB | 471 pts - 41 solves
---

# Flag proxy

> Description: I just added authentication to my flag service (server-back) thanks to a proxy (server-front), but a friend said it's useless...
> Site: [http://flag-proxy.challs.olicyber.it](http://flag-proxy.challs.olicyber.it)\
> Author: @Giotino

Looking at the challenge, we see that the website it's powered by Express.js. Looking in the source code we see that the endpoints it accepts are: `/flag` and  `/add-token`. To get the flag we have to make a request with the `?token` parameter which value will then be passed to the `Authorization` header that will be sent to the backend; which to be valid must be inside the `tokens[]` array. We can add values to `tokens[]` array by making a request at `/add-token` with the parameters: `?token` (the token we want to set) and `?auth` (some sort of password). Looking at the logic of these two endpoints, it would seem almost impossible to find an attack vector. But looking beyond the index.js's we notice that in the server-front, `http-client.js` manages and parse all the requests and responses of the application. Looking more carefully we notice how on [line 55-58](https://github.com/TeamItaly/TeamItalyCTF-2022/blob/master/FlagProxy/src/server-front/http-client.js#L55-L58) it checks that in the headers we pass, there is no LF character to protect from http request smuggling attacks. However, the program only checks for the sequence `\r\n` , but not the `\n` character alone which probably being HTTP 1.0 and an old version of node.js, could work.\
Also we need to find a way to chain requests in HTTP 1.0 (modern http-smuggling techniques won't work, i.e: `Transfer-Encoding: chunked`), this can be done by setting the header `Connection: keep-alive`.\
Let's try to craft a double smuggling request with docker container running in local to analyze logs:

<figure><img src="./assets/smuggle1.png" alt=""><figcaption></figcaption></figure>

<figure><img src="./assets/smuggle2.png" alt=""><figcaption></figcaption></figure>

It's working! Now, lets make a request to `/add-token` with an arbitrary token, to be able to write our token inside `tokens[]` array, bypassing app checks (AUTH param), and later getting the flag:

```python
import requests

url = "http://flag-proxy.challs.teamitaly.eu/flag"
token = "httpsmugglingiscool"
smuggle = f"SMUGGLE\nContent-Length: 0\nConnection: keep-alive\n\nGET /add-token?token={token} HTTP/1.0"

req1 = requests.get(url, params={"token": smuggle})
#print(req1.text)

req2 = requests.get(url, params={'token': token})
print(req2.json()['body'])
```

> flag{sanity\_check}
