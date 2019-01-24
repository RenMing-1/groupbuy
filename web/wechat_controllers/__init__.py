from flask import Blueprint

route_wechat = Blueprint('wechat', __name__)

@route_wechat.route('/wechat')
def index():
    return ''
