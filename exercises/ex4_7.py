#!/usr/bin/env python3


def solve(year):
    """Trả về tuple-2 chứa year và tên gọi can chi tương ứng. Các từ trong tên
    đề phải viết hoa các chữ cái đầu.

    Biết có 10 thiên can::

      ['giáp', 'ất', 'bính', 'đinh', 'mậu', 'kỷ', 'canh', 'tân', 'nhâm', 'quý']

    Và 12 địa chi::

      ['tý', 'sửu', 'dần', 'mão', 'thìn', 'tị', 'ngọ', 'mui', 'thân', 'dậu',
       'tuất', 'hợi']

    Năm 2017 là năm "Đinh Dậu".
    """
    Thien_can = ['Thân', 'Dậu', 'Tuất', 'Hợi', 'Tý', 'Sửu',
                 'Dần', 'Mão', 'Thìn', 'Tị', 'Ngọ', 'Mui']
    Dia_chi = ['Canh', 'Tân', 'Nhâm', 'Quý', 'Giáp',
               'Ất', 'Bính', 'Đinh', 'Mậu', 'Kỷ']

    tc = year % 12
    dc = year % 10

    result = (year, Dia_chi[dc] + " " + Thien_can[tc])

    return result


def main():
    print("Năm {0} là năm {1}".format(*solve(1696)))


if __name__ == "__main__":
    main()
