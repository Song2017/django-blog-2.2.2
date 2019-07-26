from flask import Flask, jsonify
from flask.views import MethodView
from flask import Blueprint

app = Flask(__name__)
bp = Blueprint('user', __name__, url_prefix='/userbp')


@bp.route('/')
def index():
    return 'User Module Index page'


class UserAPI(MethodView):
    '''基于调度方法的视图, 可以添加装饰器'''

    def get(self):
        return jsonify({'username': 'fake', 'avatar': 'http://test.ccc'})

    def post(self):
        return 'Unsupport'


print('app_api.py', __name__)

app.add_url_rule('/user/', view_func=UserAPI.as_view('userview'))

if __name__ == "__main__":
    print(type(UserAPI.as_view('userview')), UserAPI.as_view('userview'))
    app.run(host='0.0.0.0', port=9000)
