from sqlalchemy import create_engine, Table, MetaData, Column
from sqlalchemy import Integer, String, tuple_
from sqlalchemy.sql import select, asc, and_
from db_consts import DB_URI
'''
SQLAlchemy 支持使用表达式的方式来操作数据库
'''
eng = create_engine(DB_URI)
# databse
meta = MetaData(eng)
users = Table('Users', meta,
              Column('Id', Integer, primary_key=True, autoincrement=True),
              Column('Name', String(50), nullable=False))
print('exists', users.exists())
if users.exists():
    users.drop()
    users.create()


def execute(s):
    print('-' * 20, s)
    rs = con.execute(s)
    for row in rs:
        print(row['Id'], row['Name'])


with eng.connect() as con:
    for username in ('xiaoming', 'wanglang', 'lilei'):
        user = users.insert().values(Name=username)
        con.execute(user)
    stm = select([users]).limit(1)
    execute(stm)

    k = [(2, )]
    stm = select([users]).where(tuple_(users.c.Id).in_(k))
    execute(stm)
    stm = select([users]).where(and_(users.c.Id > 2, users.c.Id < 4))
    execute(stm)
    stm = select([users]).order_by(asc(users.c.Name))
    execute(stm)
    stm = select([users]).where(users.c.Name.like('%min%'))
    execute(stm)