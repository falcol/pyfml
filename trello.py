#!/usr/bin/env python
"""
Creates a Trello board used as timetable for new course

https://developer.atlassian.com/cloud/trello/guides/rest-api/api-introduction/
Usage: python trello.py HN2006 2020/06/25
"""
import argparse
import datetime
import os
import logging

import requests

authen = {
    "key": os.environ["TRELLO_KEY"],
    "token": os.environ["TRELLO_TOKEN"],
}
S = requests.Session()
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


def create_card(date, list_id, name):
    r = S.post(
        "https://api.trello.com/1/cards",
        params={**authen, "idList": list_id, "name": name, "due": date},
    )
    r.raise_for_status()


def main():
    argp = argparse.ArgumentParser()
    argp.add_argument("course_code", help="e.g: HN2006")
    argp.add_argument("start_date", help="e.g 2020/06/25")

    args = argp.parse_args()
    start = datetime.datetime.strptime(args.start_date, "%Y/%m/%d")
    course_code = args.course_code.upper()
    loc = "Hà Nội" if course_code.startswith("HN") else "Tp Hồ Chí Minh"

    # Create board
    board_name = "Học Python {} PYMI.vn {} timetable".format(loc, course_code)
    logger.info("Creating a new Trello board named %s", board_name)
    board_resp = S.post(
        url="https://api.trello.com/1/boards/",
        json={**authen, "name": board_name},
    )
    board_id = board_resp.json()["id"]

    # List lists
    # resp = S.get(
    #     "https://api.trello.com/1/boards/{}/lists".format(board_id),
    #     params=authen,
    # )
    # resp.json()

    logger.info("Creating two lists, one for Tuesday and other for Thurday")
    resp = S.post(
        "https://api.trello.com/1/boards/{}/lists".format(board_id),
        params={**authen, "name": "Thứ 5"},
    )
    list_thursday_id = resp.json()["id"]

    resp = S.post(
        "https://api.trello.com/1/boards/{}/lists".format(board_id),
        params={**authen, "name": "Thứ 3"},
    )
    list_tuesday_id = resp.json()["id"]
    logger.info("Creating cards for each lesson, add due date")
    count = 1
    day = start
    while count <= 12:
        # tuesday
        if day.isoweekday() == 2:
            create_card(
                date=day.strftime("%Y/%m/%d"),
                list_id=list_tuesday_id,
                name="Bài {}".format(count),
            )
            count = count + 1
        # thursday
        elif day.isoweekday() == 4:
            create_card(
                date=day.strftime("%Y/%m/%d"),
                list_id=list_thursday_id,
                name="Bài {}".format(count),
            )
            count = count + 1

        day = day + datetime.timedelta(days=1)

    logger.info("Done, URL: %s", board_resp.json()["url"])


if __name__ == "__main__":
    main()
