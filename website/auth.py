from flask import Blueprint, render_template, request, flash, redirect, url_for
auth = Blueprint('auth', __name__)


@auth.route('/login', methods=['GET', 'POST'])
def login():
    return render_template("login.html", boolean = True)

@auth.route('/logout')
def logout():
    return "<p>Logout</p>"

@auth.route('/signup',methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        email = request.form.get('email')
        firstName = request.form.get('firstName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        if len(email) < 4:
            flash('Email must be at greater than  3 characters', category='error')
        elif len(firstName) < 2:
            flash('First Name must be at greater than  1 characters', category='error')
        elif password1 != password2:
            flash('password don\'t match.', category='error')
        elif len(password1) < 7:
            flash('password must be at least 7 characters', category='error')
        else:
            # add user to database
            flash('Account created!', category='success')
            return redirect(url_for('views.home'))


    return render_template("sign_up.html")