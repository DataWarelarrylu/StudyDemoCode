import MySQLdb

mysql_host = "192.168.3.33"
mysql_user = "root"
mysql_pwd = "123456"
mysql_db_name = "mydatabase"

def query_db(sql):
    db = MySQLdb.connect(mysql_host, mysql_user, mysql_pwd, mysql_db_name)
    cur = db.cursor()
    try:
        cur.execute(sql)
        result = cur.fetchall()
    except:
        print("error: sql:" + sql)
    cur.close()
    db.close()
    return result

if __name__=='__main__':
    res =query_db('select * from t')
    print(res)