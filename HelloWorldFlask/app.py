import connexion
from flask import Flask
app = Flask(__name__)

#@app.route('/<name>')
def post_greeting(name):
    return "hello {}".format(name),200

if __name__ == '__main__':
    app = connexion.App(__name__, 9090)
    app.add_api('swagger.yaml')
    app.run()