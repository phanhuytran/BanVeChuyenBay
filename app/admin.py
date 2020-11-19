from flask import redirect
from sqlalchemy import Column, Integer, String, Boolean, Date, ForeignKey
from datetime import datetime
from app import db, admin
from sqlalchemy.orm import relationship
from flask_admin.contrib.sqla import ModelView
from flask_admin import BaseView, expose
from flask_login import UserMixin, current_user, logout_user
from enum import Enum as UserEnum

from wtforms import validators
from wtforms.fields.html5 import EmailField


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
    email = Column(String(50), nullable=False)
    phone = Column(String(50), nullable=False)
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

class Customer(db.Model, UserMixin):
    __tablename__ = 'customer'
    id = Column(Integer, primary_key=True, autoincrement=True)
    firstname = Column(String(50), nullable=False)
    lastname = Column(String(50), nullable=False)
    identity_card = Column(String(50))
    email = Column(String(50))
    phone = Column(String(50))
    def __str__(self):
        return self.name

class ModelView_Base(AuthenticatedView):
    column_display_pk = True
    can_create = False
    can_edit = True
    can_export = True
    can_delete = True
    edit_modal = True
    form_extra_fields = { 'email': EmailField("Email", validators=[validators.data_required()]) }

class ModelView_Staff(ModelView_Base):
    column_searchable_list = ('firstname', 'lastname', 'email', 'phone', 'joined_date')

class ModelView_Customer(ModelView_Base):
    column_searchable_list = ('firstname', 'lastname', 'identity_card', 'email', 'phone')


class AboutUsView(AuthenticatedView_1):
    @expose('/')
    def index(self):
        return self.render('admin/about-us.html')

class LogoutView(AuthenticatedView_1):
    @expose('/')
    def index(self):
        logout_user()
        return redirect('/admin')


admin.add_view(ModelView_Staff(Staff, db.session, category="User"))
admin.add_view(ModelView_Customer(Customer, db.session, category="User"))
admin.add_view(AboutUsView(name="About us"))
admin.add_view(LogoutView(name="Logout"))

if __name__ == "__main__":
    db.create_all()