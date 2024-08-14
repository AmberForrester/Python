from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy # ORM - Object Relational Mapper
from datetime import datetime



# create the app
app = Flask(__name__)
# configure the SQLite database, relative to the app instance folder
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///todolist.db"
# initialize the app with the extension
db = SQLAlchemy(app) # Create an object db to initialize the object.



class Todolist(db.Model):
    taskid = db.Column(db.Integer, primary_key = True) # Only one primary key. 
    task = db.Column(db.String(250), nullable = True)
    desc = db.Column(db.String(500), nullable = True)
    creation_date = db.Column(db.DateTime, default=datetime.now())
    
    def __repr__(self) -> str:
        return f'{self.taskid} - {self.task}'

with app.app_context():
    db.create_all()



@app.route("/") # Default route 
def index():
    return render_template('index.html')

# @app.route("/blog")
# def blog():
#     return "<p>This is my Blog</p>"


# @app.route("/contact")
# def contact():
#     return "<p>This is my Contact Page</p>"


if __name__ == '__main__':
    app.run(debug=True) # Development mode not production to show errors 
    