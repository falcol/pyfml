#!/usr/bin/env python3


__doc__ = """
Yêu cầu:
- Viết chương trình cứ 1 giây in ra màn hình thời gian hiện tại.
- Sau N lần thì chương trình kết thúc

Gợi ý:
time.sleep, datetime.datetime.now

Đọc thêm logging: https://pymotw.com/3/logging/index.html
"""

import time
import datetime  # NOQA

import log

logger = log.get_logger(__name__)


def get_time_sleep(N):
    """Trả về tuple chứa 2 phần tử bao gồm:
    - List chứa các điểm thời gian (string) sau N lần thực hiện
    theo yêu cầu từ ``__doc__``
    - Tổng thời gian chạy của function

    :rtype tuple:
    """
    # Sửa tên và function cho phù hợp, trả về kết quả yêu cầu.
    start = time.time()
    # NOTE: DO NOT FORMAT log by % or .format
    # http://www.familug.org/2014/09/python-logging-ung-format-log-message.html
    logger.debug("Start at %f", start)

    result = []
    # Xoá dòng sau và viết code vào đây set các giá trị phù hợp
    for i in range(N):
        now_time = datetime.datetime.now()
        time.sleep(1)
        result.append(now_time.strftime("%Y-%m-%d %H:%M:%S"))

    end = time.time()
    logger.debug("End at %f", end)
    total_time = end - start
    return (result, total_time)


def solve(N):
    """Học viên không cần chỉnh sửa trong hàm solve, chỉ thực hiện
    đổi tên lại function của mình cho phù hợp

    Hàm solve dùng cho mục đích `test`
    :rtype tuple:
    """
    result = get_time_sleep(N)
    return result


def main():
    print(solve(5))


# __name__ là một biến|name đặc biệt do Python tự tạo ra
# nó có giá trị là string "__main__" khi file được chạy bằng lệnh
# python filename.py
# và có giá trị là tên file (bỏ .py) khi được import.
if __name__ == "__main__":
    print(__name__)
    main()
