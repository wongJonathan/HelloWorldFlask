from flask import FLask
app = Flask(__name__)

@app.route('/')
def indx():
	return "<span style='color:blue'>Hello World</span>"

