from flask import Blueprint

# 定義
blue = Blueprint('blue', __name__)

# 使用
@blue.route('/')
def index():
    return "Hello Blueprint"