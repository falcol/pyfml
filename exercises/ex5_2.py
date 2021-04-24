#!/usr/bin/env python3
import copy

"""
Tips: dùng stdlib copy.deepcopy

In [14]: import copy

In [15]: d = [{'name': 'Dung', 'languages': ['C', 'Python']}]

In [16]: dnew = copy.deepcopy(d)

In [18]: dnew[0]['languages'].append('Elixir')

In [19]: dnew
Out[19]: [{'languages': ['C', 'Python', 'Elixir'], 'name': 'Dung'}]

In [20]: d
Out[20]: [{'languages': ['C', 'Python'], 'name': 'Dung'}]
"""


data = [
    {
        "name": "Hoang",
        "phone": "0988888888",
        "languages": [
            "Python",
            "C",
            "SQL",
            "HTML",
            "CSS",
            "JavaScript",
            "Golang",
        ],
    },
    {"name": "Duy", "girl_friend": "Maria"},
    {"name": "Dai", "girl_friend": "Angela"},
    {"name": "Tu"},
]


def solve(last_year_data):
    """
    Trả về list thông tin các học viên sau khi đã update sau 1 năm.
    Không thay đổi thông tin năm cũ.

    Biết các học viên đều học được các ngôn ngữ lập trình
    trong "languages" của học viên "Hoang".
    Sau đó "Hoang" học thêm được ngôn ngữ "Elixir", các học
    viên khác không biết ngôn ngữ này.
    "Tu" có bạn gái tên là "Do Anh".
    "Duy" chia thay bạn gái, không còn bạn gái nữa.

    Chú ý: code tránh dựa vào thứ tự cụ thể trong để bài.
    """
    this_year = copy.deepcopy(last_year_data)
    languagess = data[0]['languages']
    # Xoá dòng raise và Viết code vào đây set result làm kết quả
    for info in this_year:
        info.update(languages=languagess)

    this_year[0]['languages'].append("Elixir")
    this_year[1].pop('girl_friend')
    this_year[3].update(girl_friend='Do Anh')
    return this_year


def main():
    # Cho list chứa các dictionary chứa thông tin của các học viên:
    students = data
    # In ra màn hình tên học viên kèm tên bạn gái (nếu có)

    result = solve(students)  # NOQA
    # In ra các thông tin đã thay đổi so với năm trước của mỗi học viên.
    print(result)


if __name__ == "__main__":
    main()
