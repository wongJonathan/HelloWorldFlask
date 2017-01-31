import connexion
from flask import redirect,url_for, Flask,request, render_template
mac = Flask(__name__)

@mac.route('/')
def my_form():
    return render_template("input.html")

@mac.route('/', methods=['POST'])
def my_form_post():

    text = request.form['text']
    processed_text = text.upper()
    return processed_text

app = connexion.App(__name__, 9090)
app.add_api('swagger.yaml')

if __name__ == '__main__':
    app.run()