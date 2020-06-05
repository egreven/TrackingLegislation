from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def homepage():
    return render_template("homepage.html")
  
@app.route("/aboutus")
def aboutus():
    return render_template("/aboutus.html")
    
@app.route("/phydicaldistance")
def phydicaldistance():
    return render_template("/phydicaldistance.html")

"""@app.route("/mapchar")
def mapchar():
    return render_template("/mapchar.html")
"""

@app.route("/stateofemergency")
def stateofemergency():
    return render_template("/stateofemergency.html")

@app.route("/stayathome")
def stayathome():
    return render_template("/stayathome.html")

if __name__ == "__main__":
    app.run(debug=True)
