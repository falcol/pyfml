#!/usr/bin/env python3


def solve(text):
    """Thực hiện biến đổi

      input: [a, abbbccccdddd, xxyyyxyyx]
      output: [a, abb3cc4dd4, xx2yy3xyy2x]

    Giải thích: Những chữ cái không lặp lại thì output giữ nguyên chữ cái đó.
    Những chữ cái liên tiếp sẽ in ra 2 lần + số lần lặp lại liên tiếp.

    Đây là một biến thể của một thuật toán nén dữ liệu có tên Run-length
    encoding (RLE).
    NOTE: không dùng itertools.groupby
    """
    result = None
    list_word = []
    word = text[0]
    list_final = []
    # Xoá dòng sau và viết code vào đây set các giá trị phù hợp
    for char in text[1:]:
        if char is word[0]:
            word += char
        else:
            list_word.append(word)
            word = char
    list_word.append(word)

    for word in list_word:
        if word.count(word[0]) == 1:
            list_final.append(word)
        else:
            list_final.append('{}{}'.format(2 * word[0], word.count(word[0])))
    result = ''.join(list_final)
    return result


def main():
    print(solve("abbbccccdddd"))


if __name__ == "__main__":
    main()
