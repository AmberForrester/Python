from flask import Flask, render_template

app = Flask(__name__)

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
    