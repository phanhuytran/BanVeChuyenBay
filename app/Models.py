from sqlalchemy import Column, Integer, String, Date, DateTime, Boolean, ForeignKey, Enum
from datetime import datetime
from app import db, admin
from sqlalchemy.orm import relationship
from flask_admin.contrib.sqla import ModelView
from flask_login import current_user, UserMixin
from enum import Enum as UserEnum


class Base(db.Model):
    __abstract__ = True
    def __str__(self):
        return self.name


class UserRole(UserEnum):
    ADMIN = 1
    STAFF = 2


class Staff(db.Model, UserMixin):
    __tablename__ = 'staff'
    id = Column(Integer, primary_key=True, autoincrement=True)
    firstname = Column(String(50), nullable=False)
    lastname = Column(String(20), nullable=False)
    email = Column(String(50), nullable=False)
    phone = Column(String(20), nullable=False)
    avatar = Column(String(100))
    active = Column(Boolean, default=True)
    joined_date = Column(Date, default=datetime.now())
    user_role = Column(Enum(UserRole), default=UserRole.STAFF)
    account = relationship('Account', backref='staff', lazy=True)
    # def __str__(self):
    #     return self.name


class Account(db.Model, UserMixin):
    __tablename__ = 'account'
    id = Column(Integer, ForeignKey(Staff.id), primary_key=True)
    username = Column(String(20))
    password = Column(String(50))


class Customer(Base, UserMixin):
    __tablename__ = 'customer'
    id = Column(Integer, primary_key=True, autoincrement=True)
    firstname = Column(String(50), nullable=False)
    lastname = Column(String(20), nullable=False)
    identity_card = Column(String(20))
    email = Column(String(50))
    phone = Column(String(20))


class Plane(Base):
    __tablename__ = 'plane'
    idPlane = Column(Integer, primary_key=True, autoincrement=True)
    schedule = relationship('Schedule', backref='plane', lazy=True)
    seat = relationship('Seat', backref='plane', lazy=True)
    amount_Seat_Class1 = Column(Integer, nullable=False)
    amount_Seat_Class2 = Column(Integer, nullable=False)

    def __str__(self):
        return str(self.idPlane)


class Airport(Base):
    __tablename__ = 'Airport'
    idAirport = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False)


class Schedule(Base):
    __tablename__ = 'Flight Schedule'
    idFlight = Column(Integer, primary_key=True, autoincrement=True)
    departure = Column(Integer, ForeignKey(Airport.idAirport), nullable=False)
    arrival = Column(Integer, ForeignKey(Airport.idAirport), nullable=False)
    intermediate = Column(Integer, ForeignKey(Airport.idAirport))
    date = Column(DateTime, nullable=False)
    idPlane = Column(Integer, ForeignKey(Plane.idPlane))
    ticket = relationship('Ticket', backref='schedule', lazy=True)
    departure_fk = relationship('Airport', foreign_keys=[departure])
    arrival_fk = relationship('Airport',  foreign_keys=[arrival])
    intermediate_fk = relationship('Airport',  foreign_keys=[intermediate])


class RoleSeat(UserEnum):
    SEAT_CLASS1 = 1
    SEAT_CLASS2 = 2


class Seat(Base):
    __tablename__ = "seat"
    idSeat = Column(Integer, primary_key=True, autoincrement=True)
    role_seat = Column(Enum(RoleSeat), default=RoleSeat.SEAT_CLASS1)
    idPlane = Column(Integer, ForeignKey(Plane.idPlane))
    is_empty = Column(Boolean, default=True)


class Ticket(Base):
    __tablename__ ="ticket"
    idTicket = Column(Integer, ForeignKey(Seat.idSeat), primary_key=True, autoincrement=True)
    idFlight = Column(Integer, ForeignKey(Schedule.idFlight), nullable= False)
    idCustomer = Column(Integer, ForeignKey(Customer.id))
    exportTime = Column(DateTime, nullable=False)
    exportPlace = Column(String(50), nullable=False)


class AuthenticatedView(ModelView):
    def is_accessible(self):
        return current_user.is_authenticated


class ModelView_Base(AuthenticatedView):
    column_display_pk = True
    can_create = True
    can_edit = True
    can_export = True
    can_delete = True
    create_modal = True


class ModelView_Schedule(ModelView_Base):
    column_searchable_list = ('departure', 'arrival', 'date',)


admin.add_view(ModelView_Base(Plane, db.session, name="Plane"))
admin.add_view(ModelView_Schedule(Schedule, db.session, name="Flight Schedule"))


if __name__ == "__main__":
    db.create_all()


#Thêm bộ lọc
# class StaffView(ModelView_Base):
#     column_filters = ("firstname", "lastname", "username", "email", "phone", "active", "joined_date")
# class ScheduleView(ModelView_Base):
#     column_filters = ("departure", "arrival", "date", "time")