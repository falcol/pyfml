"""Crawl tất cả các bài viết có label
Python(http://www.familug.org/search/label/Python), Command, sysadmin và 10 bài
viết mới nhất ở homepage của http://www.familug.org/

Tạo file `index.html`, chứa 4 cột tương ứng cho:

```
Python | Command | Sysadmin | Latest
```

Mỗi cột chứa các link bài viết, khi bấm vào sẽ mở ra bài gốc tại FAMILUG.org
Tham khảo giao diện tại:
- https://themes.getbootstrap.com/
- http://getskeleton.com/#examples

Push code lên GitLab repo, tạo 1 GitLab Page để view kết quả.
https://pages.gitlab.io/

Nâng cao: push code lên GitHub và tạo 1 GitHub Page: https://pages.github.com/
"""

import requests
from bs4 import BeautifulSoup
import datetime
import time
import http
import json

now = datetime.datetime.now().date()
url_python = "https://www.familug.org/search/label/Python?"
url_command = "https://www.familug.org/search/label/Command?"
url_Sysadmin = "https://www.familug.org/search/label/sysadmin?"
url_new10 = "https://www.familug.org/search?"

"params: updated-max=2020-12-14&max-results=500"


def craw_data(url, params):
    r = requests.get(url, params=params)
    result = []

    if r.status_code == http.client.OK:
        tree = BeautifulSoup(markup=r.text, features="html.parser")
        Blog1 = tree.find('div', attrs={'id': 'Blog1'})
        for h3 in Blog1.find_all('h3'):
            for a in h3.find_all('a'):
                s = {"title": h3.text.replace('\n', ''),
                     "link": a.get('href')}
                result.append(s)
    else:
        print("Cannot connect to {}".format(url))

    return result


def label_Python():
    url = url_python
    params = {
            "updated-max": "{}-{}-{}".format(now.year, now.month, now.day),
            "max-results": 99999
    }

    result = craw_data(url, params)
    assert isinstance(result, list)

    return result
    pass


def label_Command():
    url = url_command
    params = {
            "updated-max": "{}-{}-{}".format(now.year, now.month, now.day),
            "max-results": 99999
    }

    result = craw_data(url, params)
    assert isinstance(result, list)

    return result
    pass


def label_Sysadmin():
    url = url_Sysadmin
    params = {
            "updated-max": "{}-{}-{}".format(now.year, now.month, now.day),
            "max-results": 99999
    }

    result = craw_data(url, params)
    assert isinstance(result, list)

    return result
    pass


def lastest():
    url = url_new10
    params = {
            "updated-max": "{}-{}-{}".format(now.year, now.month, now.day),
            "max-results": 10
    }

    result = craw_data(url, params)
    assert isinstance(result, list)

    return result
    pass


def solve():
    print('craw label python')
    py = label_Python()
    with open('label_Python.json', 'w', encoding='utf-8') as f:
        json.dump(py, f, ensure_ascii=False, indent=4)
    time.sleep(10)

    print('craw label command')
    cmd = label_Command()
    with open('label_Command.json', 'w', encoding='utf-8') as f:
        json.dump(cmd, f, ensure_ascii=False, indent=4)
    time.sleep(10)

    print('craw label sysadim')
    sys = label_Sysadmin()
    with open('label_Sysadmin.json', 'w', encoding='utf-8') as f:
        json.dump(sys, f, ensure_ascii=False, indent=4)
    time.sleep(10)

    print('craw top 10')
    last = lastest()
    with open('label_new10.json', 'w', encoding='utf-8') as f:
        json.dump(last, f, ensure_ascii=False, indent=4)

    return {"success": True}
    pass


def main():
    solve()
    print('craw done')

    return {"success": True}


if __name__ == "__main__":
    main()
