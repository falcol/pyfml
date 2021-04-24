"""
    Viết 1 script để liệt kê tất cả các GitHub repository của 1 user:

    Ví dụ với user ``pymivn``, sử dụng dữ liệu ở JSON format tại
    https://api.github.com/users/pymivn/repos

    Câu lệnh của chương trình có dạng::

        python3 githubrepos.py username

    Gợi ý:

    Sử dụng các thư viện:

    - requests
    - sys or argparse

    rtype: list
"""
import requests
import sys
import http


def get_repos(username):
    res = requests.get("https://api.github.com/users/{}/repos".format(username))
    if res.status_code == http.client.OK:
        result = res.json()
    else:
        print("Check your username or cannot connect to sever")
    return result


def solve(input_data):
    result = get_repos(input_data)
    assert isinstance(result, list)

    return result


def main():
    if len(sys.argv) < 2:
        print("Input for mat python3 filename.oy username")
        sys.exit(1)
    user_name = sys.argv[1]
    for repo in solve(user_name):
        print("REPOSITORY: ", repo["name"])
        for key, value in repo.items():
            print(key, ":", value)
        print()


if __name__ == "__main__":
    main()
