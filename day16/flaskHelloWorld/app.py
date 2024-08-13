from flask import Flask

app = Flask(__name__)

@app.route("/") # Default route 
def hello_world():
    return "<p>Hello, World!</p>" 

@app.route("/blog") # Default route 
def blog():
    return "<p>This is my blog!</p>" 

@app.route("/contact") # Default route 
def contact():
    return "<p>This is my Contact Page!</p>" 

if __name__ == '__main__':
    app.run(debug=True) # Development mode not production to show errors 
    
