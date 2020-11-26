from flask import redirect
from flask_admin import BaseView, expose
from flask_login import logout_user
from app.Models import *


class AuthenticatedView(ModelView):
    def is_accessible(self):
        return current_user.is_authenticated
class AuthenticatedView_1(BaseView):
    def is_accessible(self):
        return current_user.is_authenticated


class ModelView_Base(AuthenticatedView):
    column_display_pk = True
    can_edit = True
    can_export = True
    can_delete = True
    edit_modal = True
    # form_extra_fields = { 'email': EmailField("Email", validators=[validators.data_required()]) }


class ModelView_Staff(ModelView_Base):
    column_searchable_list = ('firstname', 'lastname', 'email', 'phone', 'joined_date')
    fast_mass_delete = True


class ModelView_Customer(ModelView_Base):
    can_create = False
    column_searchable_list = ('firstname', 'lastname', 'identity_card', 'email', 'phone')


class ModelView_Admin(ModelView_Base):
    form_columns = ('id', 'username', 'password',)


class AboutUsView(AuthenticatedView_1):
    @expose('/')
    def index(self):
        return self.render('admin/about-us.html')


class LogoutView(AuthenticatedView_1):
    @expose('/')
    def index(self):
        logout_user()
        return redirect('/admin')


admin.add_view(ModelView_Staff(Staff, db.session, category="Users"))
admin.add_view(ModelView_Customer(Customer, db.session, category="Users"))
admin.add_view(ModelView_Admin(Account, db.session, category="Users"))
admin.add_view(AboutUsView(name="About us"))
admin.add_view(LogoutView(name="Log out"))

if __name__ == "__main__":
    db.create_all()