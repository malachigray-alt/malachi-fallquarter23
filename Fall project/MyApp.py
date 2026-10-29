# import the flask libary into this flies 
from flask import Flask

# create a new flask app named "app"
app = Flask(__name__)

# create a home page for our flask app (website)
@app.route ('/') #the route for the home page 
def index():
    return "hello world "

if __name__ == '__main__':
    app.run(debug = True)