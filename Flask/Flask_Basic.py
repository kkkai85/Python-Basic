from flask import Flask, request, render_template, redirect, url_for

app = Flask(__name__)

@app.route('/login', methods = ['GET', 'POST'])
def login():
	try:
		if request.method == 'POST':
			# 使用redirect() 方法重新導向，將使用者導向到Hello() 方法並傳遞參數username
			return redirect(url_for("Hello", username = request.form.get('username')))
		
		# render_template() 會先到templates 資料夾中尋找相對應的html 檔案
		return render_template('get.html')
	except Exception as e:
		return str(e)

@app.route('/Hello/<string:username>')
def Hello(username):
	return render_template('post.html', name = username)

if __name__ == "__main__":
	app.debug = True
	app.run()
