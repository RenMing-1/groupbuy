AUTH_COOKIE_NAME = 'UserCookie'
SERVER_PORT = '5050'
SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:aaaaaaaa@localhost:3306/groupbuy'
SQLALCHEMY_TRACK_MODIFICATIONS = True
SQLALCHEMY_ENCODING = "utf8mb4"
SQLALCHEMY_BINDS = {
    'groupbuy': "mysql+pymysql://root:aaaaaaaa@localhost:3306/groupbuy"
}