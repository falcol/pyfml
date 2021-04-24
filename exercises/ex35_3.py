#!/usr/bin/env python3


def solve(N):
    """Creates a list which contains N first even integers. ``[2, 4 ...]``
    Must: use list comprehension
    Tips: list comprehension always create new list
    """
    result = None

    # Xoá dòng sau và viết code vào đây set các giá trị phù hợp
    result = [i * 2 for i in range(1, N + 1)]

    return result


def main():
    print(solve(6))


if __name__ == "__main__":
    main()
