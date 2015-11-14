""" flask 勉強用
"""
from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
	return "It Index page"

@app.route('/hello/')
@app.route('/hello/<name>/')
def hello(name=None):
		return render_template('hello.html', name=nmae)

if __name__ == '__main__':
	app.run()
