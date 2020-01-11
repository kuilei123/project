"""
数据模型
"""
import datetime

from flask_login import UserMixin
from werkzeug.security import generate_password_hash,check_password_hash

from App.extensions import db, login_manager


#用户基本资料表
class User(db.Model,UserMixin):
    __tablename__ = 'bbs_user'

    id = db.Column(db.Integer, primary_key=True,name='uid')
    username = db.Column(db.String(60), unique=True)
    password_hash = db.Column(db.String(128), nullable=False)
    usertype = db.Column(db.Integer )
    sex = db.Column(db.Integer)
    birthday = db.Column(db.Date)
    realname = db.Column(db.String(60))
    portrait = db.Column(db.String(200))
    regtime = db.Column(db.DateTime)
    qq = db.Column(db.String(15))
    signature = db.Column(db.String(300))
    answer = db.Column(db.String(300))
    isactive = db.Column(db.Integer)
    email = db.Column(db.String(300))
    lasttime = db.Column(db.DateTime)
    allowlogin = db.Column(db.Integer )
    grade = db.Column(db.Integer)

    @property
    def password(self):
        return self.password_hash


    @password.setter
    def password(self,value):
        #对密码签名
        self.password_hash=generate_password_hash(value)
    def check_password(self,password):#用户传入的密码原文
        #对比传入的密码和签名后的密码是否一致
        return check_password_hash(self.password_hash,password)


@login_manager.user_loader
def load_user(uid):
    return User.query.get(uid)


#ip黑名单
class Closeip(db.Model):
    __tablename__ = 'bbs_closeip'

    id = db.Column(db.Integer, primary_key=True)
    ip = db.Column(db.Integer, nullable=False)
    addtime = db.Column(db.Integer, nullable=False)
    overtime = db.Column(db.Integer)


#友情连接表
class Link(db.Model):
    __tablename__ = 'bbs_link'

    lid = db.Column(db.SmallInteger, primary_key=True)
    displayorder = db.Column(db.Integer, nullable=False )
    name = db.Column(db.String(30), nullable=False)
    url = db.Column(db.String(255), nullable=False)
    description = db.Column(db.String)
    logo = db.Column(db.String(255))
    addtime = db.Column(db.Integer, nullable=False)
#论坛板块表
class Category(db.Model):
    __tablename__ = 'bbs_category'

    cid = db.Column(db.Integer, primary_key=True)
    classname = db.Column(db.String(60))
    parentid = db.Column(db.Integer, nullable=False )
    replycount = db.Column(db.SmallInteger )
    motifcount = db.Column(db.SmallInteger,name="forumcount" )
    compere = db.Column(db.String(20))
    classpic = db.Column(db.String(200) )
    descrition = db.Column(db.String(200))
    orderby = db.Column(db.SmallInteger)
    lastpost = db.Column(db.String(3000))
    ispass = db.Column(db.Integer )

    def __str__(self):
        return "{}".format(self.classname)
# #帖子订单表
class Order(db.Model):
    __tablename__ = 'bbs_order'

    oid = db.Column(db.Integer, primary_key=True)
    uid = db.Column(db.Integer, nullable=False)
    tid = db.Column(db.Integer, nullable=False)
    rate = db.Column(db.Integer, nullable=False)
    addtime = db.Column(db.Integer, nullable=False)
    ispay = db.Column(db.Integer, nullable=False)



class Post(db.Model):
    __tablename__ = 'bbs_post'

    id = db.Column(db.Integer, primary_key=True)
    tid = db.Column(db.Integer)
    authorid = db.Column(db.Integer, nullable=False)
    title = db.Column(db.String(600), nullable=False)
    content = db.Column(db.String(3000), nullable=False)
    addtime = db.Column(db.Integer, nullable=False)
    addip = db.Column(db.Integer, nullable=False)
    classid = db.Column(db.Integer, nullable=False)
    replycount = db.Column(db.Integer, nullable=False )
    hits = db.Column(db.Integer, nullable=False )
    istop = db.Column(db.Integer, nullable=False )
    elite = db.Column(db.Integer, nullable=False )
    ishot = db.Column(db.Integer, nullable=False )
    rate = db.Column(db.SmallInteger, nullable=False )
    attachment = db.Column(db.SmallInteger)
    isdel = db.Column(db.Integer, nullable=False )
    style = db.Column(db.String(10))
    isdisplay = db.Column(db.Integer, nullable=False )




class Reply(db.Model):
    __tablename__ = 'bbs_reply'

    id = db.Column(db.Integer, primary_key=True)
    tid = db.Column(db.Integer)
    authorid = db.Column(db.Integer, nullable=False)
    content = db.Column(db.String, nullable=False)
    addtime = db.Column(db.Integer, nullable=False)
    addip = db.Column(db.Integer, nullable=False)
    classid = db.Column(db.Integer, nullable=False)
    isdel = db.Column(db.Integer, nullable=False)
    isdisplay = db.Column(db.Integer, nullable=False)