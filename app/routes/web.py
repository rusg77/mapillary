from flask import render_template, flash, redirect

from app import app, User, request, db
from app.forms.create_user_form import CreateUserForm


@app.route('/', methods=['GET'])
def index():
    users = User.query.all()
    return render_template('user_list.html', users=users)


@app.route('/create_user', methods=['GET', 'POST'])
def create_user_form():
    form = CreateUserForm()
    if request.method == 'POST' and form.validate():
        try:
            user = User(form.username.data, form.email.data, form.birthdate.data, form.address.data)

            db.session.add(user)
            db.session.commit()
            flash('User added!')
            return redirect('/')
        except AssertionError as e:
            flash(str(e))
    return render_template('create_user.html', form=form)
