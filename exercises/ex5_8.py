#!/usr/bin/env python3
import string


def solve():

    """Trả về biểu diễn của 20 mã ASCII từ 33 đến 53 theo format
    [(33, BIEUDIENCUA33), ...]
    Unicode codepoint của các số từ 0->9, a-z, A-Z.
    Unicode codepoint tương ứng với ký tự ``\t`` ``\n``, `` ``

    Gợi ý: dùng ``chr()``, ``ord()``.
    """
    tabcodepoint = None
    newlinecodepoint = None
    spacecodepoint = None
    twenty_ascii = []
    unicodes = []

    # Xoá dòng raise và Viết code vào đây set các giá trị phù hợp
    twenty_ascii = [(num, chr(num))
                    for num in range(33, 53)]

    tabcodepoint = ord('\t')
    newlinecodepoint = ord('\n')
    spacecodepoint = ord(' ')

    unicodes = [[chr(i) for i in range(0, 10)],
                [ord(i) for i in string.ascii_lowercase],
                [ord(i) for i in string.ascii_uppercase]]

    result = (
        twenty_ascii,
        unicodes,
        tabcodepoint,
        newlinecodepoint,
        spacecodepoint,
    )
    return result


def main():
    for part in solve():
        print(part)
        if isinstance(part, list):
            for elem in part:
                print(elem)


if __name__ == "__main__":
    main()
