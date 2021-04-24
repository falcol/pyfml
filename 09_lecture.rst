9. Crawling/Scraping
====================

Class (2)
---------

- Single inheritance.
- Using class, presents Undergraduate, and Master students
- Both have some similar attributes and some different

vars
----

Built-in function that display given object attributes.

Try::

  r = requests.get('https://pymi.vn')
  vars(s)

Exception hierarchy
-------------------

exceptions are classes.

https://docs.python.org/3/library/exceptions.html#exception-hierarchy

HTTP
----

- HTTP, client-server
- HTTP client, FireFox web console: https://developer.mozilla.org/en/docs/Tools/Web_Console
- HTTP methods: http://flask.pocoo.org/docs/0.10/quickstart/#http-methods

http server - python 3 version
-------------------------------

Run a server::

  python -m http.server

Requests
--------

- import requests; request??
- http://docs.python-requests.org/en/latest/user/quickstart/
- HTTP response codes https://developer.mozilla.org/en-US/docs/Web/HTTP/Status

Output
------

- JSON
- CSV
- DB: SQLite https://docs.python.org/3/library/sqlite3.html
  - Create
  - Select
  - Insert

BeautifulSoup4
--------------

- parsing HTML
- http://www.crummy.com/software/BeautifulSoup/bs4/doc/

Scrapy
------

Best framework for crawling: https://scrapy.org/

API
---

https://github.com/toddmotto/public-apis
