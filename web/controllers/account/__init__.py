from flask import Blueprint


route_account = Blueprint("account_page", __name__)


@route_account.route('/account')
def index():
    return ''