__doc__ = """Viết script lấy top **N** câu hỏi được vote cao nhất của tag
**LABEL** trên stackoverflow.com. In ra màn hình: Title câu hỏi,
link đến câu trả lời được vote cao nhất

Link API: https://api.stackexchange.com/docs

Dạng của câu lệnh:

  python3 so.py N LABEL"""

import requests
import sys


def top_n_question(N, tag):
    params = {
        "pagesize": N,
        "order": "desc",
        "sort": "votes",
        "tagged": tag,
        "site": "stackoverflow",
    }
    res = requests.get("https://api.stackexchange.com/2.2/questions?", params=params)

    return res.json()


def top_answer(N, tag):
    top_question = top_n_question(N, tag)
    result = []
    for i in range(int(N)):
        question_id = top_question.get("items")[i]["question_id"]
        params = {
            "pagesize": 1,
            "order": "desc",
            "sort": "votes",
            "site": "stackoverflow",
        }
        res = requests.get(
            "https://api.stackexchange.com/2.2/questions/{}/answers?".format(
                question_id
            ),
            params,
        )

        top_ans = res.json()
        question_title = top_question.get("items")[i]["title"]
        answer_id = top_ans.get("items")[0]["answer_id"]
        link_ans = "https://stackoverflow.com/a/{}".format(answer_id)
        result.append((question_title, link_ans))

    return result


def solve(N, tag):
    result = top_answer(N, tag)
    assert isinstance(result, list)

    return result


def main():
    try:
        top, label = sys.argv[1], sys.argv[2]
    except IndexError:
        print("Input format 'python3 so.py N label', N is number")

    for info in solve(top, label):
        print("Question: ", info[0])
        print("Best answer:", info[1])
        print()


if __name__ == "__main__":
    main()
