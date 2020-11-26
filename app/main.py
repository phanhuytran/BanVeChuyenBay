from app import app, login
from flask import render_template, request, redirect
from app.Models import *
from app.admin import *
from flask_login import login_user, login_required
import hashlib, os
from flask_admin import Admin

@login.user_loader
def load_user(user_id):
    return Account.query.get(user_id)

class MyView(BaseView):
    def __init__(self, *args, **kwargs):
        self._default_view = True
        super(MyView, self).__init__(*args, **kwargs)
        self.admin = Admin()
@app.route("/login-admin", methods=['GET', 'POST'])
def login_admin():
    message = ''
    if request.method == 'POST':
        username = request.form.get("username")
        password = request.form.get("password")
        password = str(hashlib.md5(password.strip().encode('utf-8')).hexdigest())
        user = Account.query.filter(Account.username == username.strip(),
                                 Account.password == password).first()
        if user:
            login_user(user=user)
        else:
            message = 'Username or password incorrect'
            return MyView().render('admin/index.html', message=message)
    return redirect("/admin")


# kiểm tra nhân viên đã tồn tại hay chưa
def check_staff(id_staff):
    staff = Staff.query.filter(Staff.id == id_staff).first()
    if staff:
        return True
    return False

# kiểm acount đã tồn tại hay chưa theo id hoặc username
def check_account(key=''):
    if key.isdigit():
        account = Account.query.filter(Account.id == key).first()
    elif key.isalpha():
        account = Account.query.filter(Account.username == key.strip()).first()

    if account:
        return True
    return False

def add_account(id_staff, username, password):
    password = str(hashlib.md5(password.strip().encode('utf-8')).hexdigest())
    user = Account(id=id_staff, username=username, password=password)
    try:
        db.session.add(user)
        db.session.commit()
        return True
    except Exception as ex:
        print(ex)
        return False

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
            message = "Password incorrect"

        elif check_account(key=username):
            message = "Username already exists"

        elif check_account(key=id_staff):
            message = 'This id staff has been registered by someone else'

        elif check_staff(id_staff=id_staff) == False:
            message = 'Id staff not already exists'

        else:
                if add_account(id_staff=id_staff,
                            username=username, password=password):
                    return redirect('/admin')
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
