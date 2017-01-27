import connexion
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World'


app = connexion.App(__name__)
app.add_api('swagger.yaml')
app.run(port=8080)