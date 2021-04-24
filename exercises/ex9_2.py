"""Viết một script kiểm tra xem các số argument đầu vào có trúng lô không
(2 số cuối trùng với một giải nào đó). Nếu không có argument nào thì print
ra tất cả các giải từ đặc biệt -> giải 7.

Lấy kết quả từ ``ketqua.net``.

Dạng của câu lệnh::

  ketqua.py [NUMBER1] [NUMBER2] [...]"""


import requests
from bs4 import BeautifulSoup
import sys
import http


def get_lottery():
    req = requests.get("http://ketqua.net")
    result = []

    if req.status_code == http.client.OK:
        tree = BeautifulSoup(markup=req.text, features="html.parser")
        tag_tbody = tree.find("table", attrs={"id": "result_tab_mb"}).find("tbody")
        for tag_tr in tag_tbody.find_all("tr"):
            tag_td = tag_tr.find_all("td")
            if len(tag_td) > 1:
                for i in range(len(tag_td)):
                    try:
                        result.append((tag_td[i]["id"][3], tag_td[i].text))
                    except KeyError:
                        continue
    else:
        print("Check your URL or sever error")

    return result


def check_lots(argument):
    nums_price = get_lottery()
    assert isinstance(nums_price, list)
    count = 0
    result = []

    for nums in argument:
        for price in nums_price:
            if nums == price[1][-2:]:
                count = count + 1
                result.append(price)

    if count == 0:
        result = nums_price

    return result


def solve(arg):
    result = check_lots(arg)
    assert isinstance(result, list)

    return result


def main():
    if len(sys.argv) < 2:
        print("Input the numbers format python3 file.py [NUMBER1] [NUMBER2]")
    input_data = sys.argv[1:]
    print("Chu y: 0 la giai dac biet")
    for win in solve(input_data):
        print("Ban trung giai {} so {}".format(win[0], win[1]))


if __name__ == "__main__":
    main()
