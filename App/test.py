import datetime
import time

# now=datetime.datetime.now()
# addtime=int(time.mktime(now.timetuple()))
# print(now)
# print('------------')
# print(addtime)
from App.extensions import db
from App.models import Post, Reply
from App.views import bbs


@bbs.route('/shuchu/')
def shuchu():
    # poo=Post.query.all()
    # print(poo)
    # for po in poo:
    #     addtime=po.addtime
    #     print(addtime)
    #     now=datetime.datetime.fromtimestamp(int(addtime))
    #     print(now)
    #     po.addtime=str(now)
    #     db.session.add(po)
    #     db.session.commit()
    return "输出"

@bbs.route('/shu/')
def shuchu():
    poo=Reply.query.all()
    print(poo)
    for po in poo:
        addtime=po.addtime
        print(addtime)
        now=datetime.datetime.fromtimestamp(int(addtime))
        print(now)
        po.addtime=str(now)
        db.session.add(po)
        db.session.commit()
    return "输出"




