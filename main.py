from flask import Flask
from flask import request
from flask import render_template

app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello"


@app.route("/get_data", methods=['GET', 'POST'])
def getData():
    if request.method == "POST":
        print(request.values)
    return render_template("main2.html")


if __name__ == "__main__":
    app.run('0.0.0.0', 8888, True)
