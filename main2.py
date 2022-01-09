from flask import Flask
from flask import templating

app = Flask(__name__)


@app.route('/')
def hello():
    return templating.render_template('main4.html')


if __name__ == "__main__":
    app.run('0.0.0.0', 8000, True)
