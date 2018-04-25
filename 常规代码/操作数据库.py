import cx_Oracle
DBLINE='name/password@127.0.0.1/dbname.sh.tz'
from sqlalchemy import create_engine
import os
# connection = cx_Oracle.Connection("acoods_public/public!#2012@192.168.1.12/acornbi.sh.tz")
# cursor = connection.cursor()
# sql = open('/home/oracle/db_info.txt').read()
# cursor.execute(sql)
# connection.commit()
engine = create_engine('oracle://lb/lb@127.0.0.1/tsbi.sh.tz')#用sqlalchemy创建引擎

def import_db(sql):
    connection = cx_Oracle.Connection(DBLINE)
    cursor = connection.cursor()
    cursor.execute(sql)
    connection.commit()

def select_db(sql):
    connection = cx_Oracle.Connection(DBLINE)
    cursor = connection.cursor()
    cursor.execute(sql)
    data = cursor.fetchall()
    return data
    connection.close()

#插入数据库
def insertData(frame,tablename):
    frame.to_sql(tablename,engine,if_exists='append',index=None)