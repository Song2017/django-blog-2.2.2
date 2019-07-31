from blinker import signal
from blinker import Namespace

started = signal('test-started')


# 信号就是在框架核心功能或者一些Flask 扩展发生动作时所发送的通知，用于帮助你解耦应用。
# blinker1.1 后支持装饰器订阅信号
@started.connect
def each(r):
    print('round:', r)


def r_two(r):
    print('round_two:', r)


# 使用connect 和I send 这两个方法不放在一个文件中，它们通过started 作为桥梁达到
# 解耦的作用
# started.connect(each)
started.connect(r_two, sender=2)
for r in range(1, 4):
    started.send(r)

# 自定义信号
web_signals = Namespace()
large_file_saved = web_signals.signal('laege_file_saved')
large_file_saved.connect(each)
for r in range(1, 3):
    large_file_saved.send(r)

# Flask中内置的信号, Flask 可以发送9 种信号，第三方的扩展也可能会有额外的信号, 我们只要添加对应的信号的订阅
# flask.template_rendered: 模板的渲染成功的时候发送这个信号
'''def log_template_renders(sender, template, context, **extra):
    sender.logger.debug('Rendering template "%s" with context %s',
                        template.name or 'string template', context)
from flask import template_rendered
template_rendered.connect(log_template_renders, app)'''
# flask.request_started: 建立请求上下文后，在请求处理开始前发送， 订阅者可以用request 之类的标准全局代理的问请求。
# flask.request_finished: 在H向应发送给客户端之前发送，可以传递response
# flask.got_request_exception: 在请求处理中抛异常时发送，异常本身会通过exception传递到订阅函数
# f1ask.request_tearing_down: 在请求销毁时发送，它总是被调用，即使发生异常
# flask.appcontent_tearing_down: 在应用上下文销毁时发送,它总是被调用.即使发生异常
