import os

from flask import Flask, render_template, request
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

app = Flask(__name__)


engine = create_engine('postgres://postgres:1337@localhost/bottlingDB')
db = scoped_session(sessionmaker(bind=engine))

@app.route("/")
def index():
    number_of_bottlings = db.execute("SELECT id FROM bottlings2 ORDER BY id DESC LIMIT 1").fetchone()
    current_bottling = db.execute("SELECT product FROM bottlings2 ORDER BY id DESC LIMIT 1").fetchone()
    previous_bottling = db.execute("SELECT product FROM bottlings2 ORDER BY id DESC LIMIT 1 OFFSET 1").fetchone()
    completed_bottlings = db.execute("SELECT count(*) FROM bottlings2 WHERE status='completed'").fetchone()
    not_completed_bottlings = db.execute("SELECT count(*) FROM bottlings2 WHERE status='not_completed'").fetchone()
    return render_template("dashboard.html", number_of_bottlings=number_of_bottlings, current_bottling=current_bottling, completed_bottlings=completed_bottlings, not_completed_bottlings=not_completed_bottlings, previous_bottling=previous_bottling)

@app.route("/bottlingruns")
def bottlingruns():
    bottling_runs = db.execute("SELECT * FROM bottlings2 ORDER BY id DESC").fetchall()
    return render_template("bottling_runs.html", bottling_runs=bottling_runs)

@app.route("/addbottling")
def addbottling():
    return render_template("add_bottling.html")

@app.route("/visitorsview")
def visitorsview():
    return render_template("visitorsview.html")

@app.route("/bottlingview")
def bottlinghall():
    bottling_runs = db.execute("SELECT * FROM bottlings2 ORDER BY id DESC").fetchall()
    return render_template("bottlingview.html", bottling_runs=bottling_runs)

@app.route("/addbottlingrun", methods=["POST"])
def addbottlingrun():
    
    #Get form information
    user_date = request.form.get("user_date")
    vatting_number = request.form.get("vatting_number")
    bottle_size = request.form.get("bottle_size")
    product = request.form.get("product")
    back_label = request.form.get("back_label")
    qty = request.form.get("qty")
    status = request.form.get("status")
    user_date_completed = request.form.get("user_date_completed")
    allow_user_edit = request.form.get("allow_user_edit")
    note = request.form.get("note")

    db.execute("INSERT INTO bottlings2 (timestamp, user_date, vatting_number, bottle_size, product, back_label, qty, status, user_date_completed, allow_user_edit, note) VALUES (current_timestamp, :user_date, :vatting_number, :bottle_size, :product, :back_label, :qty, :status, :user_date_completed, :allow_user_edit, :note)",
                {"user_date": user_date, "vatting_number": vatting_number, "bottle_size": bottle_size, "product": product, "back_label": back_label, "qty": qty, "status": status, "user_date_completed": user_date_completed, "allow_user_edit": allow_user_edit, "note": note})
    db.commit()
    return render_template("add_bottling.html", message="Bottling run added.")

# Action for complete bottling button on "Bottling View page"
@app.route("/complete_bottling_run", methods=["POST"])
def complete_bottling_run():
    # Temporary just rendering template but not working because of method=post
    return render_template("bottlingview.html")

@app.route("/edit_bottling_run", methods=["POST"])
def edit_bottling_run():
    # Temporary just rendering template but not working because of method=post
    return render_template("bottlingview.html")

if __name__ == "__main__":
    app.run()