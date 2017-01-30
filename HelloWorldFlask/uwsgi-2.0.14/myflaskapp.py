from flask import Flask
app = Flask(__name__)

@app.route('/')
def indx():
	return "<span style='color:blue'>Hello World</span>"

