#!/usr/bin/env python3

__doc__ = """
Viết script get_version nhận vào ngày ở format <month>/<day>/<year>.
VD: 03/28/16 làm parameter và in ra một version được tính theo quy luật sau:
- Version ở dạng format: <MAJOR>.<MINOR>.<PATCH>, vd: "6.9.2"
- Cách đánh version này gọi là semver http://semver.org/
- Từ ngày 09 tháng 02 năm 2016, phiên bản bắt đầu là "1.0.0"
- Mỗi 28 ngày, MAJOR lại tăng thêm 1, MINOR và PATCH set về 0
- Mỗi 7 ngày, MINOR tăng thêm 1 và PATCH sẽ set về 0
- Cứ mỗi ngày, PATCH lại tăng thêm 1.

In ra phiên bản tương ứng.

Gợi Gý: học viên sử dụng `sys.argv` hoặc module `argparse`
https://pymotw.com/3/argparse/index.html
"""

import log
import datetime
import sys

logger = log.get_logger(__name__)


def get_version(input_data):
    """Trả về tên phiên bản như yêu cầu tại ``__doc__``

    :param input_data: ngày format ở dạng <month>/<day>/<year>,
                       ví dụ: "02/03/16"
    :rtype str:
    """
    # Sửa tên và function cho phù hợp, trả về kết quả yêu cầu.
    result = None
    date = input_data.split("/")
    days = (datetime.date(
        month=int(date[0]), day=int(date[1]), year=int(date[2])
    ) - datetime.date(month=2, day=9, year=16)).days
    result = "{}.{}.{}".format(days // 28 + 1, days % 28 // 7, days % 28 % 7)
    return result


def solve(input_data):

    """Function `solve` dùng để `test`, học viên không cần chỉnh sửa gì thêm
    Chỉ thay đổi lại tên function của mình bên dưới cho phù hợp

    Gía trị trả về của hàm `solve` và `your_function` là như nhau

    :rtype str:
    """
    result = get_version(input_data)
    # Xoá dòng sau và viết code vào đây set các giá trị phù hợp
    return result


def main():
    input_data = None

    # sử dụng `sys.argv` hoặc `argparse` để gán gía trị yêu cầu
    # vào biến `input_data`
    # Xoá dòng sau và viết code vào đây set các giá trị phù hợp
    input_data = sys.argv[1]

    logger.debug("Getting version for the day %s", input_data)
    print(input_data, solve(input_data))

    for d in "02/03/16", "09/06/16", "06/23/17":
        print(d, solve(d))


if __name__ == "__main__":
    main()
