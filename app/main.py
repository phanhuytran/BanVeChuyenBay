from app import app, login
from flask import render_template, request, url_for
from app.admin import *
from flask_login import login_user
import os
from app.utils import *




@app.route("/login", methods=['POST', 'GET'])
def login_staff():
    message = ""
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password', '')
        password = hashlib.md5(password.encode('utf-8')).hexdigest()

        user = Account.query.join(Staff, Staff.id == Account.id)\
                            .filter(Account.username == username, Account.password == password)\
                            .add_columns(Account.id, Staff.user_role).first()


        if user:
            acc = Account.query.filter(Account.id == user.id).first()
            if user.user_role == UserRole.STAFF:
                login_user(user=acc)
            else:
                message = 'Username or password incorrect'
                render_template('login.html', message=message)
        else:
            message = 'Username or password incorrect'
            return render_template('login.html', message=message)
    elif request.method == 'GET':
        return render_template('login.html')

    return redirect(url_for("index"))

@app.route('/logout')
def logout_usr():
    logout_user()
    return redirect(url_for('search_flight'))


@app.route("/")
def index():
    return redirect(url_for("search_flight"))


@login.user_loader
def load_user(user_id):
    return Account.query.get(user_id)


@app.route("/login-admin", methods=['GET', 'POST'])
def login_admin():
    message = ''
    if request.method == 'POST':
        username = request.form.get("username")
        password = request.form.get("password")
        password = str(hashlib.md5(password.strip().encode('utf-8')).hexdigest())
        user = Account.query.join(Staff, Staff.id == Account.id)\
                            .filter(Account.username == username, Account.password == password)\
                            .add_columns(Account.id, Staff.user_role).first()

        if user:
            acc = Account.query.filter(Account.id == user.id).first()
            if user.user_role == UserRole.ADMIN:
                login_user(user=acc)
            else:
                message = 'Username or password incorrect'
                return MyView().render('admin/index.html', message=message)
        else:
            message = 'Username or password incorrect'
            return MyView().render('admin/index.html', message=message)
    return redirect("/admin")


@app.route("/registration", methods=['GET', 'POST'])
def register():
    message = ''
    if request.method == 'POST':
        id_staff = request.form.get('id-staff')
        username = request.form.get('username')
        password = request.form.get('password')
        confirm_password = request.form.get('confirm_password')
        avatar = request.files["avatar"]
        avatar_path = 'img/upload/%s' % avatar.filename
        avatar.save(os.path.join(app.config['ROOT_PROJECT_PATH'], 'static/', avatar_path))

        if password != confirm_password:
            message = "Password confirm incorrect"

        elif check_account(key=username):
            message = "Username already exists"

        elif check_staff(id_staff=id_staff) == False:
            message = 'Id staff not already exists'

        elif check_account(key=id_staff):
            message = 'This id staff has been registered by someone else'

        elif add_account(id_staff=id_staff,
                            username=username, password=password):
                    return redirect('/admin')
    return render_template('admin/registration.html', message=message)


@app.route("/air-ticket-sales")
def air_ticket_sales():
    return render_template("air-ticket-sales.html")
#huy

@app.route("/search-flight", methods=['POST','GET'])
def search_flight():
    airports = get_all_airport()
    if request.method == 'POST':
        departure = request.form.get('from_locate')
        arrival = request.form.get('to_locate')
        date_flight = request.form.get('date_flight')

        schedules = get_schedule(arrival_locate = arrival, depature_locate = departure,date = date_flight)
        if schedules:
            return render_template("search-flight.html", airports=airports, schedules=schedules)
        else:
            return render_template("search-flight.html", airports=airports)

    return render_template("search-flight.html",airports=airports)


@app.route("/receive-flight-schedule")
def receive_flight_schedule():
    return render_template("receive-flight-schedule.html")


@app.route("/report")
def report():
    return render_template("report.html")


if __name__ == "__main__":
    app.run(debug=True)