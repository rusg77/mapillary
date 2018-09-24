from flask import request, jsonify

from app import app, User, db


@app.route("/api/v1/users", methods=["POST"])
def create_user():
    data = request.get_json()
    username = data.get('username')
    email = data.get('email')
    birthdate = data.get('birthdate')
    address = data['address']

    try:
        user = User(username, email, birthdate, address)
        db.session.add(user)
        db.session.commit()
        return jsonify(user=user.to_json()), 200
    except AssertionError as e:
        return jsonify(error=str(e)), 400


@app.route("/api/v1/users", methods=["GET"])
def get_users():
    users = User.query.all()
    return jsonify(users=[user.to_json() for user in users])