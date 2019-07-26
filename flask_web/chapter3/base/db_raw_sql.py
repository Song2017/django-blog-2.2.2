from sqlalchemy import create_engine
from db_consts import DB_URI

eng = create_engine(DB_URI, echo=True)
with eng.connect() as con:
    # con.execute('drop table if exists users')
    # sql = 'CREATE TABLE users (id int(11) NOT NULL AUTO_INCREMENT,\
    #         name varchar(32) NOT NULL DEFAULT "name", \
    #             age tinyint(4) NULL DEFAULT 18,PRIMARY KEY (id))'

    # print(sql)
    # con.create(sql)
    con.execute("insert into users(name,age) values('xiaoming', 22)")
    con.execute("insert into users(name,age) values('wanglang', 33)")
    rs = con.execute('select * from users')
    print(rs)
    for row in rs:
        print(row)
