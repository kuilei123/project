from flask import Flask

from App.admin import dog_blueprint


from .extensions import init_app
from .settings import *

# from App.views.user import user
# from App.views import bbs,
from .views import register_blueprint

def create_app():
    app=Flask(__name__)
    app.config.from_object(config.get('develop'))

    #加载扩展
    init_app(app)

    #注册蓝图
    register_blueprint(app)

    # app.register_blueprint(user)
    # app.register_blueprint(bbs)
    dog_blueprint(app)
    return app