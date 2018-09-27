from flask import render_template

from app import app, User


@app.route("/", methods=["GET"])
def index():
    users = User.query.all()
    return render_template('user_list.html', users=users)
