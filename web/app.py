from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)
@app.route("/")
def hello(name=None):
    return render_template("home.html",name=name)

@app.route("/edinburgh")
def edinburgh(name=None):
    return render_template("edinburgh.html",name=name);

@app.route("/stirling")
def stirling(name=None):
    return render_template("stirling.html",name=name);

@app.route("/woops")
def woops(name=None):
    return render_template("woops.html",name=name);

@app.route('/handle')
def handle(name=None):
    return render_template("handle.html",name=name)

@app.route('/about')
def about(name=None):
    return render_template("about.html",name=name)

@app.route('/coldingham')
def coldingham(name=None):
    return render_template("coldingham.html",name=name)

if __name__ == "__main__":
    app.run()
