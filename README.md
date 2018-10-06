Atlas - Quick SQLMap Tamper Suggester (beta v.)
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
$ python atlas.py
```

Usage
---
```
$ python atlas.py --url http://site.com/index.php?id=10 --payload="-1234 AND 4321=4321-- AAAA" --dbms=mysql --random-agent -v
```

Example 
---
1. Run SQLMap:
```
$ python sqlmap.py -u 'http://site.com/index.php?id=10' --dbs --random-agent -v 3
```
![sqlmap](https://i.imgur.com/XP39Rqz.png)
