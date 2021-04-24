#!/usr/bin/env python3

"""
Viết 1 một trò chơi đánh đối kháng giữa 2 nhân vật. Mỗi nhân vật có tên (str),
máu (int), vũ khí.
Vũ khí chọn random khi tạo nhân vật, có damage (int) bằng lượng máu trừ đi
khi đánh trúng.

Cho 2 nhân vật lần lượt đánh nhau, print kết quả mỗi lượt đánh, print người
thắng.

"""


class Fighter:
    def __init__(self, name, HP):
        pass

    def __str__(self):
        pass

    # Add more if needed


class Weapon:
    pass


def solve(player1, player2):
    """Trả về tuple tên người thắng cuộc và lượng máu còn lại (int)"""
    result = ("", 0)

    # Xoá dòng sau và viết code vào đây set các giá trị phù hợp
    raise NotImplementedError("Học viên chưa làm bài này")

    return result


def main():
    # Thay đổi các dòng sau cho phù hợp
    player1 = Fighter()
    player2 = Fighter()
    print(solve(player1, player2))


if __name__ == "__main__":
    main()
