#!/usr/bin/env python3

NUMBER_OF_LINES = 30_000_000


def solve(output_path, n=NUMBER_OF_LINES):
    """Tạo ra 1 file chứa n dòng, các dòng lẻ chứa 30 số 1,
    các dòng chẵn chứa giá trị 2 * số dòng hiện tại.

    Sau khi tạo xong file, return result là list chứa 10 dòng đầu và 10 dòng
    cuối theo thứ tự dòng xuất hiện trước đứng trước.

    Chú ý: viết code để xử lý được nếu n lớn tùy ý (tức file sau khi tạo ra
    có thể tới 20 GB).
    Chú ý: n mặc định là 30 triệu dòng.
    """
    result = None
    line = 1
    # Xoá dòng raise và Viết code vào đây set result làm kết quả
    list_line = [True for i in range(NUMBER_OF_LINES)]
    for i in range(1, NUMBER_OF_LINES, 2):
        list_line[i] = False
    f = open('fileline.line', 'wt')
    for i in list_line:
        if i:
            f.write(30 * '1' + '\n')
        else:
            f.write(str(2 * line) + '\n')
        line = line + 1

    lines = 1
    result = []
    f = open('fileline.line', 'rt')
    for li in f:
        if lines <= 10 or lines > NUMBER_OF_LINES - 10:
            result.append(li)
        lines += 1
    #
    #
    #
    #

    import os

    # Xoá file sau khi đã xong vì file này rất lớn
    try:
        os.remove(output_path)
    except OSError as e:
        print(e)

    return result


def main():
    import tempfile

    # tên _ hàm ý rằng ta sẽ không dùng giá trị của nó - convention
    _, output_path = tempfile.mkstemp()
    print("File to write: {0}".format(output_path))

    for line in solve(output_path, n=NUMBER_OF_LINES * 10):
        print(line.rstrip())


if __name__ == "__main__":
    main()
