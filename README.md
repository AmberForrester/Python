# Python

***Get Started***
- https://www.python.org/downloads/
- https://docs.python.org/3.12/index.html
- https://docs.python.org/3.12/tutorial/index.html

> py --version
> py
>>> 2 + 4
6
>>> myvar = "Amber"
>>> myvar
'Amber'
>>> firstname = "Amber"
>>> lastname = "F"
>>> firstname + lastname
'AmberF'
>>> quit()

Python, Python Debugger, Python Indent VSCode Extensions


Ctrl + / - Toggle Line Comments 
""" """ - Multi Line String for Comments 

Day 01:
First Python Program
Understanding Module ()
Using PIP for package management

Day 02:
Comments
Variables and Data Types

Day 03:
Data Types
Operators
variable rules

Flask Documentation
https://flask.palletsprojects.com/en/1.1.x/quickstart/

https://www.geeksforgeeks.org/how-to-install-flask-in-windows/
Installing Flask on windows

Set-ExecutionPolicy unrestricted


create a root folder and run
>pip install virtualenv
>virtualenv venv
.\venv\Scripts\activate.ps1 
>pip install flask flask-sqlalchemy

create a app.py file and place the following code in it


from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


if __name__ == "__main__":
    app.run(debug=True)
   # app.run(debug=True, port=6000)
   
save and run 
>python .\app.py

[To install SQL](https://flask-sqlalchemy.palletsprojects.com/en/3.1.x/)

>pip install flask-sqlalchemy

SQL Lite viewer
https://inloop.github.io/sqlite-viewer/
