import hashlib
from flask_admin import BaseView, Admin
from sqlalchemy import desc
from sqlalchemy.orm import aliased

from app import db
from app.admin import Staff, Account
from app.Models import Schedule, Airport, Plane


class MyView(BaseView):
    def __init__(self, *args, **kwargs):
        self._default_view = True
        super(MyView, self).__init__(*args, **kwargs)
        self.admin = Admin()


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


def get_all_schedule():
    airport_1 = aliased(Airport)
    airport_2 = aliased(Airport)
    airport_3 = aliased(Airport)

    schedule = Schedule.query.join(airport_1, Schedule.arrival )\
    .join(airport_2,Schedule.departure)\
    .join(Plane, Schedule.idPlane == Plane.idPlane)\
    .add_columns(Schedule.idFlight, airport_1.name.label("(arrival airport"),
                airport_2.name.label("departure airport"),
                airport_1.locate.label("arrival locate"),
                airport_2.locate.label("depature locate"),
                Schedule.date,
                Plane.idPlane,
                Plane.amount_Seat_Class1,
                Plane.amount_Seat_Class2).order_by(desc(Schedule.date)).all()

    return  schedule