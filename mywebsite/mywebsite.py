from flask import Flask, request, session, g, redirect, url_for, abort, render_template, flash
app = Flask(__name__)

@app.route("/")
def index():
	return render_template('homepage.html')

@app.route("/hello/")
@app.route("/hello/<name>")
@app.route("/hello/", methods=['POST'])
def hello(name=None):
	if ('name' in request.form.keys()):
		name = request.form['name']
	return render_template('datapage.html', name=name)



if __name__ == "__main__":
	app.debug = True 
	app.run() 

















