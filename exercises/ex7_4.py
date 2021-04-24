#!/usr/bin/env python3
from itertools import groupby


def solve(text):
    """Thực hiện biến đổi

      input: [a, abbbccccdddd, xxyyyxyyx]
      output: [a, abb3cc4dd4, xx2yy3xyy2x]

    Giải thích: Những chữ cái không lặp lại thì output giữ nguyên chữ cái đó.
    Những chữ cái liên tiếp sẽ in ra 2 lần + số lần lặp lại liên tiếp.

    Đây là một biến thể của một thuật toán nén dữ liệu có tên Run-length
    encoding (RLE).
    NOTE: dùng itertools.groupby
    https://pymotw.com/3/itertools/
    """
    result = []
    # Xoá dòng sau và viết code vào đây set các giá trị phù hợp
    for char, chars in groupby(text):
        group_char = list(chars)
        if len(group_char) == 1:
            result.append(char)
        else:
            result.append('{}{}'.format(char * 2, len(group_char)))

    return ''.join(result)


def main():
    print(solve("abbbccccdddd"))


if __name__ == "__main__":
    main()
