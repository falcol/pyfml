#!/usr/bin/env python3


__doc__ = """
Yêu cầu:
- Lưu file ``https://raw.githubusercontent.com/hvnsweeting/states/master/salt/event/init.sls`` về máy với tên event.yaml

- Dùng pip cài thư viện PyYAML, import yaml và dùng `yaml.safe_load` để biến nội
dung trong file thành kiểu dữ liệu trên Python.

- In ra số phần tử của kiểu dữ liệu vừa tạo. Dùng thư viện json để
 `json.dump` nội dung, ghi ra một file tên là event.json trong thư mục hiện tại.

- Dùng thư viện pickle để pickle.dump nội dung trên ra file event.pkl trong
  thư mục hiện tại. Chú ý khi mở file, phải mở ở chế độ ghi ở dạng binary. Đọc
  thêm tại đây:
  https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files`

- In ra kích thước của mỗi file đã tạo.

Gợi ý: sử dụng os.stat(filename).st_size
"""  # NOQA


import json  # NOQA
import os  # NOQA
import pickle  # NOQA
import yaml  # NOQA
# import requests


def size_of_file():
    """Trả về số phần tử của kiểu dữ liệu sau khi dùng module `yaml` để load

    Thực hiện các yêu cầu tại ``__doc__``

    :rtype int:
    """
    # Sửa tên và function cho phù hợp, trả về kết quả yêu cầu.
    result = None
    # url = ("https://raw.githubusercontent.com/hvnsweeting/states/master/"
    #       "salt/event/init.sls")
    # Xoá dòng sau và viết code vào đây set các giá trị phù hợp
    # r = requests.get(url)
    # with open('event.yaml', 'wt') as f:
    #    f.write(r.text)
    yaml_path = os.path.join(os.path.dirname(__file__), 'event.yaml')
    json_path = os.path.join(os.path.dirname(__file__), 'event.json')
    pkl_path = os.path.join(os.path.dirname(__file__), 'event.pkl')

    with open(yaml_path, 'rt') as f:
        datas_yaml = yaml.safe_load(f)

    with open(json_path, 'wt') as f:
        json.dump(datas_yaml, f)

    with open(json_path) as f:
        with open(pkl_path, 'wb') as f2:
            pickle.dump(json.load(f), f2)

    result = (len(datas_yaml),
              os.stat(yaml_path).st_size,
              os.stat(json_path).st_size,
              os.stat(pkl_path).st_size)
    return result


def solve():
    """Học viên không cần viết code trong hàm `solve`, chỉ thực hiện
    đổi tên lại function của mình cho phù hợp

    :rtype int:
    """
    result = size_of_file()

    return result


def main():
    print(solve())


if __name__ == "__main__":
    main()
