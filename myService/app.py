import connexion
KEYS = {}

def print_keys():
    return KEYS

# Basically you're going to take the parameters and add it to a dictionary or list
# then return it's been made
# Parameters are coming from swagger.
def add_key(key):
    print(key['name'])
    KEYS[key['name']]=key['value']
    return 200

def get_key(name):
    value = KEYS.get(name)
    return "Name: %s Value: %s" % (name,value)

app = connexion.App(__name__, 9090)
app.add_api('swagger.yaml')

if __name__ == '__main__':
    app.run()