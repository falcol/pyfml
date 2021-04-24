from flask import Flask, render_template
import sqlite3
import ex10_1
import datetime

database = "jobs_git.db"
app = Flask(__name__)
"Link to web: https://whispering-beyond-74910.herokuapp.com/"


@app.route("/")
def create_web():
    now = datetime.datetime.now()
    if ex10_1.can_craw:
        time1 = now.strftime("%d-%m-%Y")
    else:
        time1 = "craw fail need fix"

    with sqlite3.connect(database) as conn:
        cursor = conn.cursor()
        pyjobs = []
        cursor.execute("select name, url from JOBS")
        for title, url in cursor.fetchall():
            pyjobs.append({'title': title, 'link': url})

    return render_template('index1.html', jobs=pyjobs, times=time1)


if __name__ == "__main__":
    app.run(debug=True)
