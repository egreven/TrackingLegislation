from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def homepage():
    return render_template("homepage.html")
  
@app.route("/about")
def about():
    return render_template("/about.html")
    
@app.route("/restaurants")
def restaurants():
    return render_template("/restaurants.html")

@app.route("/maptest")
def maptest():
    return render_template("/maptest.html")

if __name__ == "__main__":
    app.run(debug=True)