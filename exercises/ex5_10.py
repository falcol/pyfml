#!/usr/bin/env python3

"""
[Không bắt buộc]

Bắt đầu từ góc trên bên trái của ô có kích thước 2x2, và chỉ cho phép di chuyển
sang phải hoặc xuống dưới, có chính xác 6 đường để đi đến góc dưới bên phải.

Có bao nhiêu đường như vậy trong ô 10x10?

Kiểm tra kết quả bằng https://projecteuler.net/problem=15
"""
data = 20


def solve(input_data):
    result = None
    numerator = 1
    denominator = 1
    """result = 2n! // (n!)^2"""
    # Viết code vào đây set result làm kết quả của tính toán
    for i in range(1, input_data * 2 + 1):
        numerator = numerator * i
    for i in range(1, input_data + 1):
        denominator = denominator * i

    result = numerator // (denominator ** 2)

    return result


def main():
    num = data
    print(solve(num))


if __name__ == "__main__":
    main()
