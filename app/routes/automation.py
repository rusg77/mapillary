from flask import jsonify

from app import app, User, db


@app.route('/api/v1/automation/clean_up_users', methods=['POST'])
def clean_up_users():
    User.query.delete()
    db.session.commit()
    return jsonify(success=True)
