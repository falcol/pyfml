from flask import Flask, render_template
import json

"LINK: https://guarded-ravine-44772.herokuapp.com/"

app = Flask(__name__)


@app.route("/")
def index():
    try:
        with open('label_Python.json') as f:
            python = json.load(f)
    except (IOError, FileExistsError, FileNotFoundError):
        python = []

    try:
        with open('label_Command.json') as f:
            cmd = json.load(f)
    except (IOError, FileExistsError, FileNotFoundError):
        cmd = []

    try:
        with open('label_new10.json') as f:
            new10 = json.load(f)
    except (IOError, FileExistsError, FileNotFoundError):
        new10 = []

    try:
        with open('label_Sysadmin.json') as f:
            sys = json.load(f)
    except (IOError, FileExistsError, FileNotFoundError):
        sys = []

    return render_template('index.html',
                           python=python,
                           sysadmin=sys,
                           top10=new10,
                           command=cmd)


if __name__ == "__main__":
    app.run(debug=True)
