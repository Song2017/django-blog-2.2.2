# coding=utf-8
from flask import Flask
from flask import url_for

app = Flask(__name__)
app.debug = False
app.auto_reload = True


@app.route('/')
def hello_world():
    print(__name__)
    return 'hello world'


@app.route('/admin/<string:id>/')
def hello_admin(id):
    print(__name__)
    return id


@app.route('/about/')
def about():
    return 'about'


# url_for 构造url
@app.route('/item/<id>/')
def item(id):
    # print(url_for('item', test=44, name='namevalue'))
    return id


with app.test_request_context():
    print(url_for('item', num=1))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9000)