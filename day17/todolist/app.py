from flask import Flask, render_template, request, redirect
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
    creation_date = db.Column(db.DateTime, default=lambda: datetime.now().replace(second=0, microsecond=0))
    
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
            
            # Redirect to the GET route to avoid resbmission on refresh: 
            return redirect('/')
            
    # Query all to-do items to display them:
    myalltodolist = Todolist.query.all() # Connect to variable to throw back
     
    return render_template('index.html', myalltodolist=myalltodolist)



@app.route("/getlist") # Default route 
def getlists():
    myalltodolist = Todolist.query.all() # Connect to variable to throw back on home page.
    print(myalltodolist)
    return '<p>Get All the TO DO</p>'

@app.route("/delete/<int:taskid>") # Default route for delete when button is pressed:
def delete(taskid): # Pass the specific task to delete R/T id
    mytodo = Todolist.query.filter_by(taskid=taskid).first() # Pick up the first taskid
    db.session.delete(mytodo) # Pass the filtered taskid for deletion 
    db.session.commit()
    return redirect('/')

@app.route("/update/<int:taskid>", methods=['GET', 'POST']) # Default route for delete when button is pressed:
def update(taskid): # Pass the specific task to delete R/T id
    
    # Manage the state for updating:
    if request.method == 'POST':
        mytask = request.form['task']
        mydesc = request.form['desc']
        # Update page is now ready to call mytodo for update:
        mytodo = Todolist.query.filter_by(taskid=taskid).first() # Pick up the first taskid
        if mytodo:
        # Populate the values that are set from original input of task and description
            mytodo.task = mytask
            mytodo.desc = mydesc
            db.session.add(mytodo)
            db.session.commit()
            return redirect('/')
        
    mytodo = Todolist.query.filter_by(taskid=taskid).first()
    
    return render_template('update.html', mytodo=mytodo)

@app.route("/search", methods=['GET'])
def search(): 
    
    # Looking for a single search term: 
    query = request.args.get('query', " ")
    if query:
        
        # SQLAlchemy's filer method to search for task or desc matching the search query:
        # Filter to do list items based on the search query:
        # ilike is used for case-insensitive matching: 
        SearchResults = Todolist.query.filter(
            (Todolist.task.ilike(f'%{query}')) |    # Search query checks both with OR |
            (Todolist.desc.ilike(f'%{query}'))
        ).all()
    else:
        SearchResults = []
        
    return render_template('search.html', SearchResults=SearchResults, query=query)



if __name__ == '__main__':
    # Create db tables in an application context BEFORE creating the db:
    with app.app_context():
        db.create_all() # Seeding the data.
    app.run(debug=True) # Development mode not production to show errors. 
    