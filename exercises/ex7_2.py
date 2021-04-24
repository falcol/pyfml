#!/usr/bin/env python3
import random

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
        self.name = name
        self.HP = HP
        self.weapon = Weapon()

    def __str__(self):
        return 'Info of fighter {}: {} HP attack with {} damage {}\n'.format(
               self.name, self.HP, self.weapon.sweapon, self.weapon.sdamage)

    def Fight(self, enemy):
        if self.HP > 0:
            enemy.HP = enemy.HP - self.weapon.sdamage
            print('{} use {} attack {} HP enemy down to {}'.format(
                  self.name, self.weapon.sweapon, enemy.name, enemy.HP))

    def Champion(self):
        return '{} win with HP only {}'.format(self.name, self.HP)
    # Add more if needed


class Weapon:
    Weapons = [('Thanos_punch', 20), ('Kamehameha', 25),
               ('Excalibur', 30), ('punch_serious', 9999999)]

    def __init__(self):
        self.sweapon, self.sdamage = random.choice(self.Weapons)


def solve(player1, player2):
    """Trả về tuple tên người thắng cuộc và lượng máu còn lại (int)"""
    result = ("", 0)
    print(player1.__str__())
    print(player2.__str__())
    # Xoá dòng sau và viết code vào đây set các giá trị phù hợp
    while player1.HP > 0 and player2.HP > 0:
        player1.Fight(player2)
        player2.Fight(player1)

    if player1.HP > 0:
        print(player1.Champion())
        result = (player1.name, player1.HP)
    else:
        print(player2.Champion())
        result = (player2.name, player2.HP)

    return result


def main():
    # Thay đổi các dòng sau cho phù hợp
    player1 = Fighter(name='Alien', HP=100)
    player2 = Fighter(name='Human', HP=110)
    print(solve(player1, player2))


if __name__ == "__main__":
    main()
