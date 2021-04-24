#!/usr/bin/env python3
import os
import sys


def solve(*args, **kwargs):
    """Return tuple chứa
    - Đường dẫn tới code của module `os`
    - list chứa các attribute của os và sys
    - Số dòng trong module `os`

    Biết dir(object) sẽ trả về tất cả thuộc tính (attribute) của object đó.
    Module cũng là object.

    In [11]: import os

    In [12]: len(dir(os))
    Out[12]: 284
    """

    result = None

    # Xoá dòng sau và viết code vào đây set các giá trị phù hợp
    link_to_os = os.path.abspath(os.__file__)
    os_att = dir(os)
    sys_att = dir(sys)
    with open(link_to_os) as f:
        line_os_file = sum(1 for i in f)
    result = (link_to_os, os_att, sys_att, line_os_file)
    return result


def main():
    print(solve())


if __name__ == "__main__":
    main()
