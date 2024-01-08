

'''
The Flask class constructor only requires the name of the primary module or package to be interpreted as the 
application. Flask uses this to figure out where the application is and where its important files will be. 
As some of these will not be .py files and might not have any .py files in their directory, Flask needs to set 
up an application structure that allows it to see everything.

For the purposes of our curriculum, this argument will always be __name__, which refers to the name of the 
current module.

'''
from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Welcome to my page!</h1>'

@app.route('/<string:username>')
def user(username):
    return f'<h1>Profile for {username}</h1>'

if __name__ == '__main__':
    app.run(port=5555, debug=True)
