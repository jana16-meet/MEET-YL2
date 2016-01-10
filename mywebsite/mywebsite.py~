from flask import Flask, request, session, g, redirect, url_for, abort, render_template, flash
app = Flask(__name__)

@app.route("/")
def homepage():
	return render_template('homepage.html')


@app.route("/contactme/")
def contactme():
	return render_template('contactme.html')

@app.route("/aboutme/")
def aboutme():
	return render_template('aboutme.html')



@app.route("/datapage/", methods=['POST'])
def hello(name=None):
	if ('name' in request.form.keys()):
		name = request.form['name']
		return render_template('datapage.html', name=name)


if __name__ == "__main__":
	app.debug = True 
	app.run() 

















