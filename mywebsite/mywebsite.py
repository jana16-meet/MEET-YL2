from flask import Flask, request, session, g, redirect, url_for, abort, render_template, flash
app = Flask(__name__)

@app.route("/") 
def homepage():
	return render_template('homepage.html')

@app.route("/aboutme/")
	def homepage():
	return render_template('aboutme.html')

@app.route("/contactme/", methods=['POST'])
def contactme():
	facebook = request.form['facebook']
	name = request.form["name"]
	return render_template('datapage.html', name=name, facebook=facebook)











