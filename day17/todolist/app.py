from flask import Flask, render_template, request
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
    creation_date = db.Column(db.DateTime, default=datetime.now().replace(second=0, microsecond=0))
    
    def __repr__(self) -> str:
        return f'{self.taskid} - {self.task} - {self.desc}'



@app.route("/", methods=['GET', 'POST']) # Default route 
def index():
    
    # Only process the form data if it is a POST request:
    if request.method == 'POST':
        mytask = request.form['task']
        mydesc = request.form['desc']
        # print('Checking the post method'), checking the requests. 
        # print(request.form['task'])
        # print(request.form['desc'])
    
    # Only add the todo if task and description are not empty:
        if mytask and mydesc:
            todo = Todolist(task=mytask, desc=mydesc)
            db.session.add(todo)
            db.session.commit()
            
    # Query all to-do items to display them:
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
    