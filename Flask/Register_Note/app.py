from flask import Flask

from basic.form import form

app = Flask(__name__)

if __name__ == '__main__':
    app.debug = True
    app.run()