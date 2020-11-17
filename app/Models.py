from flask import redirect
from sqlalchemy import Column, Integer, String, Boolean, Date, ForeignKey
from datetime import datetime
from app import db, admin
from sqlalchemy.orm import relationship
from flask_admin.contrib.sqla import ModelView
from flask_admin import BaseView, expose
from flask_login import UserMixin, current_user, logout_user

class Schedule(db.Model):
    __tablename__ = 'Flight Schedule'
    idFlight = Column(Integer, primary_key=True, autoincrement=True)
    departure = Column(String(50), nullable=False)
    arrival = Column(String(50), nullable=False)
    date = Column(Date, nullable=False)
    time = Column(String(50), nullable=False)
    def __str__(self):
        return self.name

class AuthenticatedView(ModelView):
    def is_accessible(self):
        return current_user.is_authenticated

class ModelView_Base(AuthenticatedView):
    column_display_pk = True
    can_create = True
    can_edit = True
    can_export = True
    can_delete = True

admin.add_view(ModelView_Base(Schedule, db.session, name="Flight Schedule"))

if __name__ == "__main__":
    db.create_all()

#Thêm bộ lọc
# class StaffView(ModelView_Base):
#     column_filters = ("firstname", "lastname", "username", "email", "phone", "active", "joined_date")
# class ScheduleView(ModelView_Base):
#     column_filters = ("departure", "arrival", "date", "time")