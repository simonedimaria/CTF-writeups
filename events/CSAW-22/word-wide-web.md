---
description: WEB | 54 pts - 406 solves
---

# Word Wide Web

> Description: Isn't the Word Wide Web a fascinating place to be in? Words.. so many words.. all linked... NOTE: The flag doesn't have a wrapper. It needs to be wrapped with curly brackets and please put CTF in front of the curly brackets.

This challenge wasn't much about a particular vulnerability but more like a sanity-check. Opening http://web.chal.csaw.io:5010 it shows up a website with a lot of words and fake links, but viewing source code (view-source:http://web.chal.csaw.io:5010/) and searching for href values you actually see the real links. You don't have much more apart from the fact that there were a cookie "solChain" that tracked all your endpoint visits made in chronological order, and description says that words are all linked, so it was clear that the sequence in which you clicked the links was important. I made a script that scraped the REAL links in the page and visiting it until it shows up something different.​

{% file src="../../.gitbook/assets/WordWideWeb.py" %}
Exploit
{% endfile %}

> CTF{w0rdS\_4R3\_4mAz1nG\_r1ght}
