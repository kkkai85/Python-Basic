"""
Blueprint 主要用來整合專案的路由，使用上就是定義、關聯、使用、註冊。
"""
from flask import Flask, Blueprint

# 關聯
from view import blue

app = Flask(__name__)

#註冊
app.register_blueprint(blue, url_prefix = '/blue')

if __name__ == '__main__':
    app.debug = True
    app.run()