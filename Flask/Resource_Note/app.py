from flask import Flask
from flask_restful import Api

from view import Stores

app = Flask(__name__)
api = Api(app)

# 透過api.add_resource() 方法來設定路由，第二個參數是將Resource 綁定到url /store
api.add_resource(Stores, '/store')

if __name__ == "__main__":
    app.debug = True
    app.run()