#!/usr/bin/env python3


def sumall(*input_data):
    """Viết function ``sumall`` tính tổng của tất cả các argument (int, float,
    hoặc string) được gọi. Thay input_data bằng code phù hợp.
    """
    my_sum = sum(float(i) for i in input_data)
    return my_sum


def solve():
    result = None
    # Xoá dòng sau và viết code vào đây set các giá trị phù hợp
    result = sumall(1, 2, 3, 4.5, 5, " 6 ")
    result2 = sumall(1, 2, 3, 4.5, 5, 9, " 6 ")

    return result, result2


def main():
    print(solve())


if __name__ == "__main__":
    main()
