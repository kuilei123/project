"""
视图层，管理用户的信息，包括用户的信息维护，登录，注册
"""
from _md5 import md5

from flask import Blueprint, request, redirect, url_for, render_template, make_response, session
from flask_login import login_user, logout_user

from App.extensions import db
from App.models import User
from App.tools import VerifyCode

user=Blueprint('user',__name__,url_prefix='/user')


#用户登录
@user.route('/login/',methods=['GET','POST'])
def login():
    if request.method == 'POST':
        username=request.form.get("username")
        password=request.form.get("password")
        user=User.query.filter(User.username==username).first()
        password1=md5(password.encode("utf8")).hexdigest()
        password2=user.check_password(password)
        # 在数据库里查询用户
        # user=User.query.filter(User.username==username,User.password_hash==password).first()

        if user and password1==user.password_hash:
            #将用户信息写入session
            login_user(user)
        elif user and password2:
            login_user(user)
        #跳转首页
        return redirect(url_for("bbs.index"))
    else:
        #登录界面展示
        return '登录'




@user.route('/logout/')
def logout():
    #退出登录
    logout_user()
    return redirect(url_for("bbs.index"))



# #立即注册渲染页面
# @user.route('/register/')
# def register():
#     return render_template('index/reg.html')

#验证码展示
@user.route('/show/')
def show_yzm():
    vc=VerifyCode()
    # print(session['code'])
    result=vc.generate()
    session['code'] = vc.code
    # print(session['code'])
    response=make_response(result)
    response.headers['content-type']='image/png'
    return response


#用户注册
@user.route('/register/',methods=['GET','POST'])
def register():
    if request.method=='GET':
        return render_template('index/reg.html')
    elif request.method=='POST':
        username=request.form.get("username")
        password=request.form.get("password")
        repassword=request.form.get("repassword")
        mail=request.form.get("mail")
        yzm=request.form.get("yzm")
        code=session['code']
        user = User.query.filter(User.username == username).first()
        if not user and password==repassword and yzm==code:
            user=User()
            user.username=username
            user.password=password
            # md5加密
            # user.password_hash=md5(password.encode("utf8")).hexdigest()
            user.email=mail
            db.session.add(user)
            db.session.commit()
            return redirect(url_for("bbs.index"))

        else:
            return redirect(url_for("user.register"))
    else:
        return "请提供正确的操作"



