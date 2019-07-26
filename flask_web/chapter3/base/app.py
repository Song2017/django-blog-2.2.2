from flask import Flask

import app_api

app = Flask(__name__)

app.register_blueprint(app_api.bp)
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=9000)
