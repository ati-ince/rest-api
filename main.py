from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__) # application starting point
db = SQLAlchemy(app)

@app.route('/')
def index():
    return 'Welcome to the index !!!'


# run the applicatuin
if __name__ == '__main__':
    app.run()