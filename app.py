from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("admin.html")

@app.route("/admin.html")
def admin():
    return render_template("admin.html")

@app.route("/bottling_runs.html")
def bottlingruns():
    return render_template("bottling_runs.html")

@app.route("/add_bottling.html")
def addbottling():
    return render_template("add_bottling.html")
