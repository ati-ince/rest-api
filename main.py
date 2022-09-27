from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__) # application starting point
db = SQLAlchemy(app)

@app.route('/')
def index():
    return 'HELLLOOO !!!!'


# run the applicatuin
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)