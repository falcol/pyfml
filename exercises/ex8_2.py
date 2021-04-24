#!/usr/bin/env python3

__doc__ = """
Yêu cầu: Viết script ex8_2.py:
- khi gọi với -h tên_file sẽ in ra 10 dòng đầu tiên của file (h == head),
- khi gọi với -t tên_file sẽ in ra 10 dòng cuối cùng của file (t == tail).

Usage::

  ex8_2.py -h file_path

  -> Print 10 first lines of file_path

  ex8_2.py -t file_path

  -> Print 10 last lines of file_path

Use ``sys.argv``
Đọc thêm: https://pymotw.com/3/sys/runtime.html#command-line-arguments
"""


import log
import sys

logger = log.get_logger(__name__)


def read_file_ht(option, n, file_path):
    """Trả về list chứa n dòng tùy thuộc vào `option` (-t hoặc -h) sau khi
    đọc dữ liệu từ file

    :param option: tùy chọn để in ra các dòng đầu hoặc cuối: -h hoặc -t
    :param file_path: đường dẫn tới file
    :rtype list:
    """
    # Sửa tên và function cho phù hợp, trả về kết quả yêu cầu.
    result = []
    lines = 1
    # Xoá dòng sau và viết code vào đây set các giá trị phù hợp
    with open(file_path) as f:
        all_line = int(sum(1 for line in f))

        with open(file_path) as f:
            if option == '-h':
                for line in f:
                    if lines <= n:
                        result.append(line)
                    lines = lines + 1

            if option == '-t':
                for line in f:
                    if lines > (all_line - n):
                        result.append(line)
                    lines = lines + 1
    return result


def solve(option, file_path):
    """Hàm `solve` sử dụng với mục đích `test`, học viên không cần chỉnh
    sửa gì thêm

    :param option: tùy chọn để in ra các dòng đầu hoặc cuối: -h hoặc -t
    :param file_path: đường dẫn tới file
    :rtype list:
    """
    # Lưu ý: sửa lại tên function của mình cho phù hợp
    logger.debug("Using %s option with file %s", option, file_path)

    # gán n = giá trị đọc được ở file ../setup.cfg trong section [flake8]
    # key max-line-length
    import os
    import configparser

    parse = configparser.ConfigParser()
    with open(os.path.join(os.path.dirname(__file__), "../setup.cfg")) as f:
        print(f.read())

    p_file = os.path.join(os.path.dirname(__file__), "../setup.cfg")
    parse.read(p_file)
    n = int(parse['flake8']['max-line-length'])
    print(n, type(n))
    # Sử dụng thư viện có sẵn configparser
    # https://docs.python.org/3.6/library/configparser.html
    # để đọc file config này,
    # đây là định dạng tương tự file INI hay gặp trên Windows.
    # Các chương trình thường sử dụng các file cấu hình để chứa các giá trị
    # cần thay đổi cho chương trình thay vì viết trực tiếp vào file code
    # bao gồm cả user, password... Khi dùng git, tránh commit các file cấu
    # hình có chứa password để tránh bị lộ.
    # các file cấu hình thường theo format INI nói trên, JSON hay YAML.
    # Một cách khác hay gặp trên các hệ điều hành khác Windows là đọc từ
    # "biến môi trường" (environment var) bằng cách truy cập os.environ['KEY'].
    result = read_file_ht(option, n, file_path)

    return result


def main():
    option, file_path = None, None

    # Viết code xử lí truyền 2 argument `option` và `file_path` bên dưới
    # option: tùy chọn để in ra các dòng đầu hoặc cuối: -h hoặc -t
    # file_path: đường dẫn tới file
    # Gợi ý: sử dụng sys.argv
    # Xoá dòng sau và viết code vào đây set các giá trị phù hợp
    option, file_path = sys.argv[1], sys.argv[2]
    lines = solve(option, file_path)
    for line in lines:
        line = line.rstrip()
        print(line)


if __name__ == "__main__":
    main()
