"""
板块管理
"""
from flask import Blueprint

cat = Blueprint('cat',__name__,url_prefix='/admin')

@cat.route('/cat')
def index():
    return "板块管理"