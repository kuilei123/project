
from .user import user
from .views import bbs

def register_blueprint(app):
    app.register_blueprint(user)
    app.register_blueprint(bbs)