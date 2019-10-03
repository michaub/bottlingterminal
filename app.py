from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

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

@app.route("/addbottlingrun", methods=["POST"])
def addbottlingrun():
    
    #Get form information
    date = request.form.get("date")
    product = request.form.get("product")
    back_label = request.form.get("back_label")
    qty = request.form.get("qty")
    user_edit = request.form.get("user_edit")
    bottle_size = request.form.get("bottle_size")
    status = request.form.get("status")
    date_completed = request.form.get("date_completed")
    comment = request.form.get("comment")

    #Add bottling run
    bottlingrun = BottlingRun(date=date, product=product, back_label=back_label, qty=qty, user_edit=user_edit, bottle_size=bottle_size, status=status, date_completed=date_completed, comment=comment)
    db.session.add(bottlingrun)
    db.session.commit()
    return render_template("success.html")
    
#Do I need below??
class Bottlings(db.Model)
    __tablename__ = "bottlings"
    id = db.Column(db.Integer, primary_key = True)
    timestamp = db.Column(db.String, nullable = False)
    date = db.Column(db.Date, nullable = False)
    product = 
