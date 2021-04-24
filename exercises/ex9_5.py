"""Viết script dùng API tạo 1 Trello board với 2 list "Thứ 3", "Thứ 5",
và tạo 12 card ứng với 12 buổi học của lớp, có set due date ứng với các ngày
học.

Ví dụ kết quả: https://trello.com/b/yEskTV8S/h%E1%BB%8Dc-python-
h%C3%A0-n%E1%BB%99i-pymivn-hn2006-timetable

API: https://developer.atlassian.com/cloud/trello/
guides/rest-api/api-introduction/

https://developer.atlassian.com/cloud/trello/rest/#api-boards-post
https://developer.atlassian.com/cloud/trello/rest/#api-lists-post
https://developer.atlassian.com/cloud/trello/rest/#api-cards-post """

import requests


key = "Has been delete"
token = "Has been delete"


def create_board(name):
    url = "https://api.trello.com/1/boards/"

    query = {"key": key, "token": token, "name": "{}".format(name)}

    resp = requests.request("POST", url, params=query)
    board_id = resp.json()["shortUrl"].split("/")[-1].strip()

    return board_id


def create_list(board_id, name):
    url = "https://api.trello.com/1/boards/{}/lists".format(board_id)
    query = {
        "key": key,
        "token": token,
        "name": "{}".format(name),
    }

    resp = requests.request("POST", url, params=query)
    list_id = resp.json()["id"]

    return list_id


def create_card(list_id, card_name, due):
    url = "https://api.trello.com/1/cards"
    query = {
        "key": key,
        "token": token,
        "idList": list_id,
        "name": card_name,
        "due": due,
    }

    response = requests.request("POST", url, params=query)
    card_id = response.json()["id"]

    return card_id


def solve():
    board_id = create_board("PymiTimetable")
    weekdays = ["Thứ 5", "Thứ 3"]
    days = [
        [
            ("Bài 1", "2020/06/25"),
            ("Bài 3", "2020/07/02"),
            ("Bài 5", "2020/07/09"),
            ("Bài 7", "2020/07/16"),
            ("Bài 9", "2020/07/23"),
            ("Bài 11", "2020/07/30"),
        ],
        [
            ("Bài 2", "2020/06/30"),
            ("Bài 4", "2020/07/07"),
            ("Bài 6", "2020/07/14"),
            ("Bài 8", "2020/07/21"),
            ("Bài 10", "2020/07/28"),
            ("Bài 12", "2020/08/04"),
        ],
    ]

    for w in weekdays:
        list_name = create_list(board_id, w)
        idx = weekdays.index(w)
        for card_name in days[idx]:
            create_card(list_name, card_name[0], card_name[1])

    return

    pass


def main():
    solve()
    print("Done")
    print("link:https://trello.com/b/V9Dp0bxY/pymitimetable")
    pass


if __name__ == "__main__":
    main()
