# coding=utf-8
HOSTNAME = '123mysqldb20190724.mysql.rds.aliyuncs.com'
DATABASE = 'mysqldb'
USERNAME = 'dbuser'
PASSWORD = 'dbuser_13'
DB_URI = 'mysql+pymysql://{}:{}@{}/{}'.format(USERNAME, PASSWORD, HOSTNAME,
                                              DATABASE)
