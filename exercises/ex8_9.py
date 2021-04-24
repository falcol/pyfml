#!/usr/bin/env python3

__doc__ = """
Yêu cầu:
- Tìm và in ra tổng số dòng của mỗi loại file (kể cả thư mục con,
dựa vào phần mở rộng abc.py và xyz.py là cùng loại) khi thực hiện lệnh:

    ex8_9.py `duong_dan_toi_thu_muc`

- Mặc định là thư mục hiện tại: PATH = '.'

Gợi ý: sử dụng `os.walk` để duyệt vào thư mục con.

Yêu cầu nâng cao:
- Trong thư mục hiện tại nếu tìm thấy file là python module
in ra màn hình tên của các function trong đó

Gợi ý: sử dụng 2 module `inspect` và `importlib`
``from inspect import isfunction``
``from importlib import import_module``


Tham khảo thêm cho Sysadmin

- Explore more stdlib for system: os, shutil, subprocess, thread, multiprocess,
  smtp, imap, pop3
- Explore 3rd lib: psutils, paramiko, twisted, gevent
- Use tools written in python: diamond, graphite, saltstack, odoo, sentry,
  fabric, shinken, django CMS, trac, buildbot
"""


import log
import sys
import os
from inspect import getmembers, isfunction
from importlib import import_module
logger = log.get_logger(__name__)
PATH = "."


def line_in_file(input_data):
    """Trả về `dict` chứa tổng số dòng của từng loại file trong thư
    mục hiện tại (bao gồm cả thư mục con) theo format:

        result = {
            ".py": 1234,
            ".txt": 5678,
            ...
        }

    Lưu ý:
    - Nếu file không đọc được, gán số dòng bằng 0

    :param input_data: đường dẫn tới thư mục
    :rtype dict:
    """
    # Sửa tên và function cho phù hợp, trả về kết quả yêu cầu.
    result = {}
    # Xoá dòng sau và viết code vào đây set các giá trị phù hợp
    for root, direct, files in os.walk(input_data, topdown=True):
        for file in files:
            path_file = os.path.join(root, file)
            file_extension = path_file[path_file.rfind('.'):]
            if file_extension not in result:
                result[file_extension] = 0
            try:
                with open(file, 'r') as f:
                    result[file_extension] += sum(1 for line in f)
            except (IOError, UnicodeDecodeError):
                continue

    return result


def find_func(input_data):
    for root, direct, files in os.walk(input_data, topdown=True):
        for file in files:
            fil = os.path.splitext(file)[0]
            try:
                if import_module(fil):
                    module = import_module(fil)
                    functions_list = [o for o in getmembers(module)
                                      if isfunction(o[1])]
                    print(functions_list)
            except (ModuleNotFoundError, NameError,
                    IOError, UnicodeDecodeError):
                continue
    return


def solve(input_data):
    """Function `solve` dùng để `test`, học viên không cần chỉnh sửa gì thêm
    Chỉ thay đổi lại tên function của mình bên dưới cho phù hợp

    Gía trị trả về của hàm `solve` và `your_function` là như nhau

    :param input_data: đường dẫn tới thư mục
    :rtype dict:
    NOTE: nếu test xảy ra exception, mở file test và sửa lại cho đúng,
    bạn đã học hết Python rồi.
    """

    logger.debug("Statically analysing directory %s", input_data)
    result = line_in_file(input_data)
    return result


def main():
    path = PATH  # thư mục hiện tại

    # sử dụng `sys.argv` hoặc `argparse` để gán gía trị yêu cầu vào biến `path`
    # Xoá dòng sau và viết code vào đây set các giá trị phù hợp
    path = sys.argv[1]
    find_func(path)
    print(solve(path))


if __name__ == "__main__":
    main()
