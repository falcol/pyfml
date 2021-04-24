#!/usr/bin/env python3

import os
import json  # NOQA


data = os.path.join(os.path.dirname(__file__), "salt_contributors.json")


def contributors(datapath):
    """Trả về list chứa các dictionary chứa data về các contributor bao gồm
    các key: login, html_url và contributions.
    Nếu html_url nào bị thiếu, tạo html_url mới bằng
    "https://github.com/" + login tương ứng.
    """
    # Sửa function cho phù hợp, trả về kết quả yêu cầu.
    # Xoá dòng sau và viết code vào đây set các giá trị phù hợp
    with open(datapath) as f:
        contributors_data = json.load(f)

    result = []
    for info in contributors_data:
        if 'html_url' not in info or info['html_url'] == "":
            info.update(html_url="https://github.com/" + info['login'])
        contributor = {'login': info['login'],
                       'html_url': info['html_url'],
                       'contributions': info['contributions']}
        result.append(contributor)
    return result


def solve(input_data):
    result = contributors(input_data)

    return result


def main():
    """Truy cập đường dẫn
    https://api.github.com/repos/saltstack/salt/contributors?page=4 Lưu lại
    thành file salt_contributors.json.
    Sử dụng JSON để chuyển dữ liệu thành dữ liệu trong Python.
    File đã được lưu sẵn trong thư mục này - link để đây để học viên biết
    dữ liệu lấy từ đâu.
    """
    datafile = data

    for d in solve(datafile):
        print("User: {login} - URL {html_url} - {contributions}".format(**d))


if __name__ == "__main__":
    main()
