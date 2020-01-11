"""
应用扩展模块：用于加载各种类的实例，数据库快，邮件，bootstap
"""
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db=SQLAlchemy()
migrate=Migrate()
login_manager=LoginManager()
#初始化
def init_app(app):
    db.init_app(app)
    migrate.init_app(app)
    login_manager.init_app(app)

    #设置登录端点
    login_manager.login_view='user.login' #蓝图名.视图函数名