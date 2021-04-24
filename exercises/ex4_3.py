#!/usr/bin/env python3
import string


def solve(words):
    """Trả về list chứa điểm tương ứng của các từ trong `words`

    Nếu a b c d (không phân biệt chữ hoa thường) .... lần lượt bằng 1 2 3 4 ...
    thì từ ``attitude`` có giá trị bằng 100.
    (http://www.familug.org/2015/05/golang-tinh-tu-cung-9gag.html)

    Gợi ý::

      import string
      print(string.ascii_lowercase)
    """

    result = None
    result = []
    sum_word = 0
    # Xoá dòng sau và viết code vào đây set các giá trị phù hợp
    # Cach 1
    # for word in words:
    #    for w in word.lower():
    #        sum_word += ord(w) - 96
    #    result.append(sum_word)
    #    sum_word = 0

    # Cach 2
    for word in words:
        for w in word.lower():
            sum_word += string.ascii_lowercase.index(w) + 1
        result.append(sum_word)
        sum_word = 0
    return result


def main():
    words = [
        "numpy",
        "django",
        "saltstack",
        "discipline",
        "Python",
        "FAMILUG",
        "pymi",
    ]

    print(solve(words))


if __name__ == "__main__":
    main()
