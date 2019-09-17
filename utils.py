from flask_admin import AdminIndexView, expose
from flask_security import login_required

class MyView(AdminIndexView):
            @expose('/')
            @login_required
            def index(self):
                return self.render('admin/index.html')
