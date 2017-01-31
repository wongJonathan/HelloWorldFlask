import connexion

def get_world():
    return "Hello World Get"

def post_world():
    return "Hello World Post"

app = connexion.App(__name__, 9090)
app.add_api('swagger.yaml')

if __name__ == '__main__':
    app.run()