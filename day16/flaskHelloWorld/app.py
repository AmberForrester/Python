from flask import Flask, render_template

app = Flask(__name__)

@app.route("/") # Default route 
def index():
    return render_template('index.html')

@app.route("/jobsearch")
def jobsearch():
    return render_template('jobsearch.html')

@app.route("/joblisting")
def joblisting():
    return render_template('joblisting_json.html')
   
@app.route("/terms")
def terms():
    return render_template('terms.html')

@app.route("/privacy")
def privacy():
    return render_template('privacy.html')
    
@app.route("/contact")
def contact():
    return render_template('contact.html')   

if __name__ == '__main__':
    app.run(debug=True) # Development mode not production to show errors 
    
