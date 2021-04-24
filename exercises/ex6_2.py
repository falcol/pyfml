#!/usr/bin/env python3


def Tuple_N(data, N):
    # Sửa tên, set giá trị return
    result = [tuple(data[i: i + N])
              for i in range(0, len(data), N)
              if len(data[i: i + N]) == N]

    return result
    pass


def solve(list_data, N):
    """ Chia input_data thành các tuple chứa N phần tử (chunk a list).
    Nếu tuple cuối không đủ phần tử thì bỏ đi.
    """
    result = None

    # Xoá dòng sau và viết code vào đây set các giá trị phù hợp

    # sửa thành tên function phù hợp
    result = Tuple_N(list_data, N)

    return result


def main():
    li = ["meo", "bo", "ga", "cho", "chim", "gau", "voi"]
    print(solve(li, 2))


if __name__ == "__main__":
    main()
