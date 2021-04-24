#!/usr/bin/env python3


def solve(numbers):
    """Create a list that each element is 2 times of each given numbers.

    Use map, not listcomps. Example of using map

    In [2]: map(lambda x: x+1, [1,2,3,4,5])
    Out[2]: [2, 3, 4, 5, 6]
    """

    result = None

    # Xoá dòng sau và viết code vào đây set các giá trị phù hợp
    result = map(lambda x: x * 2, numbers)

    return list(result)


def main():
    print(solve(range(10)))


if __name__ == "__main__":
    main()
