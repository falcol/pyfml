#!/usr/bin/env python3


def solve(numbers):
    """Tìm phần tử lớn nhất của list số nguyên `numbers`
    Không sử dụng function `max`, `sorted`
    """
    assert isinstance(numbers, list)
    result = None

    # Xoá dòng sau và viết code vào đây set các giá trị phù hợp
    max_num = numbers[0]
    for num in numbers[1:]:
        if num > max_num:
            max_num = num
    result = max_num
    return result


def main():
    print(solve([-1, 5, 9, 6, 2, 1]))


if __name__ == "__main__":
    main()
