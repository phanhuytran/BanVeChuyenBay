from app import app, login
from flask import render_template, request, redirect
from app.Models import *
from app.admin import *
from flask_login import login_user, login_required
import hashlib, os

@login.user_loader
def load_user(user_id):
    return Account.query.get(user_id)

@app.route("/login-admin", methods=['GET', 'POST'])
def login_admin():
    if request.method == 'POST':
        username = request.form.get("username")
        password = request.form.get("password")
        password = str(hashlib.md5(password.strip().encode('utf-8')).hexdigest())
        user = Account.query.filter(Account.username == username.strip(),
                                 Account.password == password).first()
        if user:
            login_user(user=user)
    return redirect("/admin")

def check_user(username):
    users = Account.query.all()
    for user in users:
        if user.username == username:
            return False
    return True

def add_user(firstname, lastname, username, password, email, phone, avatar):
    password = str(hashlib.md5(password.strip().encode('utf-8')).hexdigest())
    user = Staff(firstname=firstname, lastname=lastname, email=email, phone=phone, avatar=avatar)
    user1 = Account(username=username, password=password)
    try:
        db.session.add(user)
        db.session.add(user1)
        db.session.commit()
        return True
    except Exception as ex:
        print(ex)
        return False

@app.route("/registration", methods=['GET', 'POST'])
def register():
    message = ''
    if request.method == 'POST':
        firstname = request.form.get('firstname')
        lastname = request.form.get("lastname")
        username = request.form.get('username')
        password = request.form.get('password')
        confirm_password = request.form.get('confirm_password')
        email = request.form.get('email')
        phone = request.form.get('phone')
        avatar = request.files["avatar"]
        avatar_path = 'img/upload/%s' % avatar.filename
        avatar.save(os.path.join(app.config['ROOT_PROJECT_PATH'], 'static/', avatar_path))
        if check_user(username) and password == confirm_password:
            if add_user(firstname=firstname, lastname=lastname,
                        username=username, password=password,
                        email=email,phone=phone, avatar=avatar_path):
                return redirect('/admin')
        else:
            message = "Register unsuccessfully"
    return render_template('admin/registration.html', message=message)

@app.route("/air-ticket-sales")
def air_ticket_sales():
    return render_template("air-ticket-sales.html")

@app.route("/search-flight")
def search_flight():
    return render_template("search-flight.html")

@app.route("/receive-flight-schedule")
def receive_flight_schedule():
    return render_template("receive-flight-schedule.html")

@app.route("/report")
def report():
    return render_template("report.html")

if __name__ == "__main__":
    app.run(debug=True)