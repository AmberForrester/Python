from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy # ORM - Object Relational Mapper
from datetime import datetime

# Create the app:
app = Flask(__name__)

# Configure the SQLite database, relative to the app instance folder:
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///todolist.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the app with the extension:
db = SQLAlchemy(app) # Create an object db to initialize the object.
class Todolist(db.Model):
    taskid = db.Column(db.Integer, primary_key = True) # Only one primary key. 
    task = db.Column(db.String(250), nullable = True)
    desc = db.Column(db.String(500), nullable = True)
    creation_date = db.Column(db.DateTime, default=datetime.now())
    
    def __repr__(self) -> str:
        return f'{self.taskid} - {self.task} - {self.desc}'




@app.route("/") # Default route 
def index():
    todo = Todolist(task='reading a book', desc='Dotcom Secrets')
    db.session.add(todo)
    db.session.commit()
    myalltodolist = Todolist.query.all() # Connect to variable to throw back 
    return render_template('index.html', myalltodolist=myalltodolist)

@app.route("/getlist") # Default route 
def getlists():
    myalltodolist = Todolist.query.all() # Connect to variable to throw back on home page.
    print(myalltodolist)
    return '<p>Get All the TO DO</p>'



if __name__ == '__main__':
    # Create db tables in an application context BEFORE creating the db:
    with app.app_context():
        db.create_all() # Seeding the data.
    app.run(debug=True) # Development mode not production to show errors. 
    