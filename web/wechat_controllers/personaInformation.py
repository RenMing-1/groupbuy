from flask import Blueprint, request, jsonify

from web.wechat_controllers import route_wechat

@route_wechat.route("/perInfo/")
def get_infomation():
    return 'success'














