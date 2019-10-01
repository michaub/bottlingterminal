from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("dashboard.html")

@app.route("/bottlingruns")
def bottlingruns():
    return render_template("bottling_runs.html")

@app.route("/addbottling")
def addbottling():
    return render_template("add_bottling.html")

@app.route("/visitorsview")
def visitorsview():
    return render_template("visitorsview.html")

@app.route("/bottlingview")
def bottlinghall():
    return render_template("bottlingview.html")