# coding=utf-8
import random

from flask import Flask, g, render_template, request
from ext import db
from users import User


app = Flask(__name__, template_folder='../../templates')
app.config.from_object('config')
db.init_app(app)

# Flask 的4个上下文变量
# 1. flask. current_app:  应用上下文, 它是当前app 实例对象。
# 2. flask.g: 应用上下文, 处理请求时用作临时存储的对象。
# 3. flask.request: 请求上下文。它封装了客户端发出的HTTP 请求中的内容。
# 4. flask.session: 请求上下文。 它存储了用户会话。

# • before_firsCrequest: 在处理第一次请求之前执行。
# • before_request: 在每次请求前执行。
# • teardown_appcontext: 不管是否有异常， 注册的函数都会在每次请求之后执行。
# 79
# • contexCprocessor : 上下文处理的装饰器，返回的字典中的键可以在上下文巾使用。
# • template_filter: 在使用Jinja2 模板的时候可以方便地注册过滤器。
# • errorhandler : errorhandler 接收状态码，可以向定义返回这种状态码的响应的处理
# 方法


def get_current_user():
    users = User.query.all()
    return random.choice(users)


@app.before_first_request
def setup():
    print(1, 'before_first_request')
    # db.drop_all()
    # db.create_all()
    # fake_users = [
    #     User('xiaoming', 'xiaoming@dongwm.com'),
    #     User('dongwweiming', 'dongwm@dongwm.com'),
    #     User('admin', 'admin@dongwm.com')
    # ]
    # db.session.add_all(fake_users)
    # db.session.commit()

@app.before_request
def before_request():
    # 获取全局可访问的 g.user
    print(2, 'before_request')
    # g.user = get_current_user()


@app.teardown_appcontext
def teardown(exc=None):
    print(6, 'teardown_appcontext')
    # if exc is None:
    #     db.session.commit()
    # else:
    #     db.session.rollback()
    # db.session.remove()
    # g.user = None


@app.context_processor
def template_extras():
    print(4, 'context_processor')
    g.user = 123
    return {'enumerate': enumerate, 'current_user': g.user}


@app.errorhandler(404)
def page_not_found(error):
    print('after before_request', 'errorhandler')
    return 'This page does not exist', 404


@app.template_filter('capitalize')
def reverse_filter(s):
    print(5, 'template_filter')
    return s.capitalize()


@app.route('/users/')
def user_view():
    print(3, 'route user_view')
    name = request.args.get('name')
    users = [
        User('xiaoming', 'xiaoming@dongwm.com'),
        User('dongwweiming', 'dongwm@dongwm.com'),
        User('admin', 'admin@dongwm.com')
    ]
    # users = User.query.all()
    return render_template('chapter3/user.html', users=users)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9000)