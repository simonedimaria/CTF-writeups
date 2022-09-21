---
description: REV | 52 pts - 440 solves
---

# DockREleakage

> Description: A breach occurred and some files have been leaked. One of the leaked files named `dockREleakage.tar.gz` contains an image of one of the company's components. An anonymous hacker has reached out to me and beware me that there is some serious mistake in my build image process. The hacker implies that sensitive information should be handled carefully. However, I couldn't find the mistake by myself. Please help me!

The challenge provides you `dockREleakage.tar.gz`, so pretty straight forward:\
`tar xvf dockREleakage.tar --directory dockREleakage`\
cd into folder and you'll find different layers of a docker image. In the first json you'll find the history of docker commands and in particular these two are useful for us:

```json
    {
        "created": "2022-09-03T07:46:12.680399343Z",
        "created_by": "/bin/sh -c echo \"ZmxhZ3tuM3Yzcl9sMzR2M181M241MTcxdjNfMW5mMHJtNDcxMG5fdW5wcjA=\" \u003e /dev/null",
        "empty_layer": true
    },
    {
        "created": "2022-09-03T07:46:13.319972067Z",
        "created_by": "/bin/sh -c cat p-flag.txt \u003e tmp.txt; rm -rf flag.txt p-flag.txt; mv tmp.txt flag.txt; echo \"\" \u003e\u003e flag.txt"
    },
```

First command == first part of the flag, that is clearly a base64 encoded string:

```shell
$ echo "ZmxhZ3tuM3Yzcl9sMzR2M181M241MTcxdjNfMW5mMHJtNDcxMG5fdW5wcjA=" | base64 -d
flag{n3v3r_l34v3_53n5171v3_1nf0rm4710n_unpr0
```

Second command == second part of the flag, unsuccessful attempts to hide the flag as you can find them in the various layers inside the `layer.tar`

```bash
$ cd 928ab519cd995aeae5eced3dbe4b7e86c8bc7f7662ef0f73e59c2f30b2b3b8e4
$ tree layer && cat layer/chal/flag.txt
layer
└── chal
    └── flag.txt
    
73c73d_w17h1n_7h3_d0ck3rf1l3}
Find the rest of the flag by yourself!
```

{% hint style="info" %}
Check out also this nice tool to explore docker image layers:\
[https://github.com/wagoodman/dive](https://github.com/wagoodman/dive)
{% endhint %}

> flag{n3v3r\_l34v3\_53n5171v3\_1nf0rm4710n\_unpr073c73d\_w17h1n\_7h3\_d0ck3rf1l3}
