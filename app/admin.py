from flask import redirect
from sqlalchemy import Column, Integer, String, Boolean, Date, ForeignKey
from datetime import datetime
from app import db, admin
from sqlalchemy.orm import relationship
from flask_admin.contrib.sqla import ModelView
from flask_admin import BaseView, expose
from flask_login import UserMixin, current_user, logout_user
from enum import Enum as UserEnum

from wtforms import validators, PasswordField
from wtforms.fields.html5 import EmailField, TelField


class UserRole(UserEnum):
    USER = 1
    ADMIN = 2

class AuthenticatedView(ModelView):
    def is_accessible(self):
        return current_user.is_authenticated
class AuthenticatedView_1(BaseView):
    def is_accessible(self):
        return current_user.is_authenticated

class Staff(db.Model, UserMixin):
    __tablename__ = 'staff'
    id = Column(Integer, primary_key=True, autoincrement=True)
    firstname = Column(String(50), nullable=False)
    lastname = Column(String(50), nullable=False)
    email = Column(String(50))
    phone = Column(String(50))
    avatar = Column(String(100))
    active = Column(Boolean, default=True)
    joined_date = Column(Date, default=datetime.now())
    account = relationship('Account', backref='staff', lazy=True)
    def __str__(self):
        return self.name

class Account(db.Model, UserMixin):
    __tablename__ = 'account'
    id = Column(Integer, ForeignKey(Staff.id), primary_key=True, autoincrement=True)
    username = Column(String(100), nullable=False)
    password = Column(String(100), nullable=False)

class ModelView_Base(AuthenticatedView):
    column_display_pk = True
    can_create = False
    can_edit = True
    can_export = True
    can_delete = True
    edit_modal = True
    column_searchable_list = ('firstname', 'lastname', 'phone', 'email', 'joined_date')
    form_extra_fields = {
        'email': EmailField("Email", validators=[validators.data_required()])
    }

class AboutUsView(AuthenticatedView_1):
    @expose('/')
    def index(self):
        return self.render('admin/about-us.html')

class LogoutView(AuthenticatedView_1):
    @expose('/')
    def index(self):
        logout_user()
        return redirect('/admin')

admin.add_view(ModelView_Base(Staff, db.session, name="Staff"))
admin.add_view(AboutUsView(name="About us"))
admin.add_view(LogoutView(name="Logout"))

if __name__ == "__main__":
    db.create_all()

# class Customer(db.Model, UserMixin):
#     __tablename__ = 'customer'
#     id = Column(Integer, primary_key=True, autoincrement=True)
#     fullname = Column(String(50), nullable=False)
#     username = Column(String(100), nullable=False)
#     password = Column(String(100), nullable=False)
#     email = Column(String(50))
#     phone = Column(String(50))
#     active = Column(Boolean, default=True)
#     joined_date = Column(Date, default=datetime.now())
#     def __str__(self):
#         return self.name