from flask import Flask,request, render_template
app = Flask(__name__)

@app.route('/')
def submitting_form():
    return render_template("input.html")

@app.route('/',methods=['POST'])
def submitting_form_post():
    text = request.form['text']
    return text
