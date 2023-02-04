from flask import Flask
from random import randint

app = Flask(__name__)


@app.route('/')
def main_page():
    return "Hello, world!"


@app.route('/random_list')
def random_list_page():
    _list = []
    for _ in range(10):
        _list.append(randint(1, 100))
    _list.sort()
    return _list


@app.route('/get_my_name/<int:age>/<string:name>')
def get_my_name(age: int, name: str):
    return f"Your name is {name} and you are {age} old."


if __name__ == "__main__":
    app.run()
