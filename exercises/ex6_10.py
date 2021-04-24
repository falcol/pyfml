#!/usr/bin/env python3

"""
Bài này không bắt buộc.
"""


def read_code_is_more_important_than_write():
    """Read those code
    https://github.com/familug/FAMILUG/tree/master/Python
    """
    pass


def rprint(n):
    """Hàm đệ quy (recursive function) in ra màn hình từ 1 -> n.
    Tham khảo: http://pymi.vn/blog/print-recursively/
    """
    if n == 0:
        return
    else:
        rprint(n - 1)
        print(n)


def pe_02():
    """
    Mỗi số (term) mới trong chuỗi (sequence) Fibonacci được tạo ra bằng cách
    cộng 2 số trước đó. Bắt đầu với 1 và 2, 10 số đầu sẽ là:

    1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

    Kiểm tra tất cả các số trong chuỗi Fibonacci mà giá trị < 4 triêu, tính
    tổng của các số chẵn (sum of the even-valued terms).

    Kiểm tra kết quả tại: https://projecteuler.net/problem=2
    """
    a, b = 0, 1
    result = 0
    for i in range(1_000_000):
        a, b = a + b, a
        if a > 4_000_000:
            break
        if a % 2 == 0:
            result += a
    return result


def move_hanoi_tower(disk, source, dest, spare):
    """
    source --->>> spare --->>> dest

    Viết hàm đệ quy (recursive function) giải bài toán tháp Hà Nội lừng danh
    https://en.wikipedia.org/wiki/Tower_of_Hanoi
    hoặc https://vi.wikipedia.org/wiki/Th%C3%A1p_H%C3%A0_N%E1%BB%99i

    In ra từng bước chuyển đĩa.
    """
    if disk > 0:
        if disk == 1:
            print('Chuyen {} sang {}'.format(source, spare))
            return
        move_hanoi_tower(disk - 1, source, spare, dest)
        move_hanoi_tower(1, source, dest, spare)
        move_hanoi_tower(disk - 1, dest, source, spare)


def main():
    rprint(9)
    print(
        "Tổng của các số fibonacci chẵn nhỏ hơn 4 triệu là"
        ": {}".format(pe_02())
    )
    move_hanoi_tower(3, "A", "C", "B")


if __name__ == "__main__":
    main()
