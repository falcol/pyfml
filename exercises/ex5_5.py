#!/usr/bin/env python3
import os


filename = "input_5_5.txt"
datafile = os.path.join(os.path.dirname(__file__), filename)
MAGIC_NUMBER = 20200000


def solve(inputfile, N=5):
    """
    Đọc danh sách học viên từ file `inputfile`.
    https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files

    Biết những bạn có tên bắt đầu bằng chữ `D` sẽ ngồi phòng thi số N,
    các bạn có tên bắt đầu chữ `H` ngồi phòng thi số N+1, và các bạn còn lại,
    nếu có tên kết thúc là `ng` sẽ ngồi cùng phòng các bạn tên `H`, còn lại
    ngồi cùng phòng `D`.
    Tất cả các học viên đều sinh năm 1990.
    Mã học viên được tính bằng: hash(NAME) % MAGIC_NUMBER
    (chú ý số này mỗi lần chạy sẽ khác nhau).
    Ví dụ: mã học viên của 'Dung' là: hash('Dung') % MAGIC_NUMBER

    Trả về result là list các tuple chứa
    (mã sinh viên, tên học viên, năm sinh, phòng thi), sắp xếp
    theo thứ tự tên học viên.
    """
    result = []
    list_student = []
    year = 1990
    room = 0
    # Xoá dòng raise và Viết code vào đây set result làm kết quả
    with open(inputfile) as f:
        for names in f:
            list_student.append(names.rstrip())
    list_student.sort()

    for names in list_student:
        if names.startswith('H') and names.endswith('ng'):
            room = N + 1
        else:
            room = N
        msv = hash(names) % MAGIC_NUMBER
        info = (msv, names, year, room)
        result.append(info)

    return result


def main():
    filename = datafile
    # Cho danh sách học viên students
    for msv, *ignore, room in solve(filename):
        print(msv, room)
        print("DEBUG", ignore, type(ignore), len(ignore))


if __name__ == "__main__":
    main()
