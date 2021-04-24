#!/usr/bin/env python3

"""
a, b, c là các số nguyên dương nhỏ hơn 10, biết a + b/c = 10

In ra list chứa các bộ số thỏa mãn điều kiện trên (a, b, c có thể trùng nhau).

Ví dụ:

- output: [[9, 1, 1], ...]
"""


def solve():
    """Trả về list chứa các list là các bộ số thỏa mãn đề bài

    Ví dụ:
        [[9, 1, 1], ..., [1, 9, 1]]

    Lưu ý: kết quả từng list con trả về với a giảm dần, b và c tăng dần
    """
    result = None
    ls_full = []
    # Xoá dòng sau và viết code vào đây set các giá trị phù hợp
    for b in range(1, 10):
        for c in range(1, 10):
            if b % c == 0:
                a = 10 - (b // c)
                ls_num = [a, b, c]
                ls_full.append(ls_num)
    result = sorted(ls_full, key=lambda n: f"{10 - n[0]}{n[1]}{n[2]}")
    return result


def main():
    print(solve())


if __name__ == "__main__":
    main()
