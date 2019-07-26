from db_consts import HOSTNAME, DATABASE, PASSWORD, USERNAME
import pymysql

''' 需要commit的sql要一条一条的执行'''
try:

    # 打开数据库连接
    db = pymysql.connect(HOSTNAME, USERNAME, PASSWORD, DATABASE)

    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = db.cursor()

    # 使用 execute()  方法执行 SQL 查询
    cursor.execute("SELECT VERSION()")
    # 使用 fetchone() 方法获取单条数据.
    data = cursor.fetchone()
    print("Database version : %s " % data)

    # 使用 cursor() 方法创建一个游标对象 cursor
    # 使用 execute() 方法执行 SQL，如果表存在则删除
    cursor.execute("DROP TABLE IF EXISTS EMPLOYEE")

    # 使用预处理语句创建表
    sql = """CREATE TABLE EMPLOYEE (
            FIRST_NAME  CHAR(20) NOT NULL,
            LAST_NAME  CHAR(20),
            AGE INT,
            SEX CHAR(1),
            INCOME FLOAT )"""
    cursor.execute(sql) 
    # SQL 插入语句
    sql3 = "INSERT INTO EMPLOYEE(FIRST_NAME, \
        LAST_NAME, AGE, SEX, INCOME) \
        VALUES ('%s', '%s',  %s,  '%s',  %s)" % ('Mac', 'Mohan', 20, 'W', 2000)
    sql2 = "INSERT INTO EMPLOYEE(FIRST_NAME, \
        LAST_NAME, AGE, SEX, INCOME) \
        VALUES ('%s', '%s',  %s,  '%s',  %s)" % ('Win', 'Mohan', 20, 'W', 2000)
    sql = """INSERT INTO EMPLOYEE(FIRST_NAME,
            LAST_NAME, AGE, SEX, INCOME)
            VALUES ('Mac2', 'Mohan', 20, 'M', 2000)""" 
    try:
        # 执行sql语句
        cursor.execute(sql)
        cursor.execute(sql2)
        cursor.execute(sql3)
        # 提交到数据库执行
        db.commit()
    except Exception as e:
        # 如果发生错误则回滚
        db.rollback()

    # SQL 查询语句
    sql = "SELECT * FROM EMPLOYEE \
        WHERE INCOME > %s" % (1000)
    try:
        # 执行SQL语句
        cursor.execute(sql)
        # 获取所有记录列表
        results = cursor.fetchall()
        for row in results:
            fname = row[0]
            lname = row[1]
            age = row[2]
            sex = row[3]
            income = row[4]
            # 打印结果
            print("fname=%s,lname=%s,age=%s,sex=%s,income=%s" %
                  (fname, lname, age, sex, income))
    except Exception as e:
        print("Error: unable to fetch data", e)

    # SQL 更新语句
    sql_update = "UPDATE EMPLOYEE SET AGE = AGE + 3 WHERE SEX = '%c'" % ('M')
    print(sql_update)
    try:
        # 执行sql语句
        cursor.execute(sql_update)
        # 提交到数据库执行
        db.commit()
    except Exception as e:
        # 如果发生错误则回滚
        db.rollback()
    # SQL 删除语句
    sql_del = "DELETE FROM EMPLOYEE WHERE FIRST_NAME = %s" % ('Win')
    try:
        # 执行sql语句
        cursor.execute(sql_del)
        # 提交到数据库执行
        db.commit()
    except Exception as e:
        # 如果发生错误则回滚
        db.rollback()
except Exception as e:
    print(e)
finally:
    print('db close')
    # 关闭数据库连接
    if db:
        db.close()
