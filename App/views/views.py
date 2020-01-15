import datetime
import time
import uuid


from flask import Blueprint, render_template, request
from flask_login import login_required
from sqlalchemy import func

from App.models import Category, db, User, Link, Post

bbs=Blueprint('bbs',__name__)


@bbs.route('/')
@bbs.route("/<int:cid>")
def index(cid=0):
    # print(cid)
    """

    :param cid: 缺省值是0，展示所有板块信息，否则展示指定板块信息
    :return:
    """
    #查询大板块数据
    big_category=Category.query.filter(Category.parentid==0).all()
    small_cegegory = Category.query.filter(Category.parentid != 0).all()
    # print(big_category)
    # print("---"*100)
    # print(small_cegegory)
    #统计帖子数，回复数
    # res=db.session.execute("select sum(replycount)")

    counts = db.session.query(func.sum(Category.replycount), func.sum(Category.motifcount)).group_by(
        Category.parentid).having(Category.parentid == 0).all()
    replycount=counts[0][0]
    motifcount=counts[0][1]
    # print(replycount,motifcount)


    # 会员数
    user_count=User.query.count()

    #新会员
    new_user = User.query.order_by(-User.id).limit(1).first()
    # print(new_user)

    #友情链接
    links=Link.query.order_by(-Link.lid).all()
    # print(links)

    #指定代码块
    if cid!=0:
        for big in big_category:
            if big.cid==cid:
                the_big=big
                break
        # return render_template("index/index.html",big_category=big_category,small_cegegory=small_cegegory,the_big=the_big)
        return render_template("index/index.html",**locals())
    else:
        return render_template("index/index.html",**locals())




@bbs.route('/list/<int:cid>/')
def list_post(cid):
    posts=Post.query.filter(Post.classid==cid).all()
    for post in posts:
        if not post.isdel:
            id=post.id
            tid=post.tid
            authorid=post.authorid
            title=post.title
            content=post.content
            addtime=post.addtime
            addip=post.addip
            replycount=post.replycount
            hits=post.hits
            istop=post.istop
            elite=post.elite
            ishot=post.ishot
            rate=post.rate
            attachment=post.attachment
            style=post.style
            isdisplay=post.isdisplay
        else:
            continue

    return render_template("index/list.html",**locals())


@bbs.route('/publish/',methods=['GET','POST'])
@login_required
def publish_post(cid,rate):
    if request.method=='GET':
        return render_template('index/addc.html')
    if request.method=='POST':

        tid=uuid.uuid4()
        authorid=db.session.id
        title=request.form.get('title')
        content=request.form.get('content')
        now=datetime.datetime.now()
        addtime=int(time.mktime(now.timetuple()))
        addip=request.remote_addr
        classid=cid
        rate=rate


    return "发帖"



