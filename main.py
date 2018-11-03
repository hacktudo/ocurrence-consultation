from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route("/bombeiro")
def fireman():
    return render_template("bombeiros.html", ocurrences=['asd'])

@app.route("/policia")
def police():
    return render_template("bombeiros.html", ocurrences=['asd'])