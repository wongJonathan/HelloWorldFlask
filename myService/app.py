import connexion
from flask import Flask


"""
For inputing name
@app.route('/<name>')
def post_greeting(name):
    return "hello {}".format(name),200
"""

def post_world():
    return "hello world"

app = connexion.App(__name__, 9090)
app.add_api('swagger.yaml')

application = app.app

if __name__ == '__main__':
    app.run()