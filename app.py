from flask import Flask
from flask_migrate import Migrate
from models import db


#app instance
app = Flask(__name__)

#sqlalchemy configurations
app.config['SQLALCHEMY_DATABASE URI'] =  'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = 'False'

migrate = Migrate(app, db)

db.init_app(app)


@app.route("/")
def index():
    return "hello world"



@app.route("/about")
def about():
    return "hello from about"


if __name__== "__main__":
    app.run(port =5000, debug=True)