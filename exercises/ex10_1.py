"""Làm một website tuyển dụng.

Lấy dữ liệu các job từ: https://github.com/awesome-jobs/vietnam/issues

Lưu dữ liệu vào một bảng ``jobs`` trong SQLite. Xem ví dụ: https://docs.python.org/3/library/sqlite3.html

Dùng Flask tạo website hiển thị danh sách các jobs khi vào đường dẫn ``/``.
Khi bấm vào mỗi job (1 link), sẽ mở ra trang chi tiết về jobs (giống như trên
các trang web tìm viêc)."""

import sqlite3
import requests
import schedule

url_api = "https://api.github.com/repos/awesome-jobs/vietnam/issues?"
database = "jobs_git.db"


def craw_to_db(db_name, url):
    "database"
    conn = sqlite3.connect(db_name)
    cur = conn.cursor()
    try:
        conn.execute("Create table JOBS (name text, url text, id integer);")
    except sqlite3.OperationalError:
        print("Table jobs has (id, name, url)")
    conn.commit()

    "Craw data from api github"
    page, data = 1, []

    while True:
        r = requests.get(url, params={"page": page})
        if r.json() == []:
            break
        for info in r.json():
            id_info = info["id"]
            cur.execute("select id from JOBS where id ='" + str(id_info) + "'")
            id_sql = cur.fetchone()
            conn.commit()
            if id_sql is None or id_info != id_sql[0]:
                data.append((info["id"], info["title"], info["html_url"]))
        page = page + 1

    "save to db"
    for info in data:
        conn.execute("insert into jobs values (?, ?, ?);", info)
        conn.commit()
    conn.close()

    return {"Success": True}


def solve(db, url):
    craw_to_db(db, url)

    return {"Success": True}


def can_craw():
    r = requests.get(url_api)
    if r.status_code == 200:
        return True


def main():
    url = url_api
    db = database
    print("Craw data to database")
    solve(db, url)
    print("done")

    return {"Success": True}


schedule.every().day.at("05:00").do(main)


if __name__ == "__main__":
    schedule.run_pending()
