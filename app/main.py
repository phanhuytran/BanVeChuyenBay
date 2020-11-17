from app import app, login
from flask import render_template, request, redirect
from app.Models import *
from app.admin import *
from flask_login import login_user, login_required
import hashlib

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

def add_user(firstname,lastname, username, password, email, phone):
    user = Staff(firstname=firstname, lastname=lastname, email=email, phone=phone)
    user1 = Account(username=username, password=password)
    db.session.add(user)
    db.session.add(user1)
    db.session.commit()

@app.route("/registration", methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form.get('username')
        firstname = request.form.get('firstname')
        lastname = request.form.get("lastname")
        password = request.form.get('password')
        passwordconfirm = request.form.get('passwordconfirm')
        email = request.form.get('email')
        phone = request.form.get('phone')
        message='Register unsuccessfully'
        if check_user(username) and password == passwordconfirm:
            add_user(firstname=firstname,lastname=lastname,
                     username=username, password=password,
                     email=email, phone=phone)
            message='Register successfully'
        return render_template('admin/registration.html', message=message)
    return render_template("admin/registration.html")

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