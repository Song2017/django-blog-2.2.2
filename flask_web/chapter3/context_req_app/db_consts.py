# coding=utf-8
HOSTNAME = 'mysqldb20190724.mysql.rds.aliyuncs.com'
DATABASE = 'mysqldb'
USERNAME = 'dbuser'
PASSWORD = 'dbuser_123'
DB_URI = 'mysql+pymysql://{}:{}@{}/{}'.format(USERNAME, PASSWORD, HOSTNAME,
                                              DATABASE)
