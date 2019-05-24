import pymysql
import  settings
conn=pymysql.Connect(**settings.parameters)
cursor=conn.cursor(cursor=pymysql.cursors.DictCursor)
sql='select sno,sname from student'
res=cursor.execute(sql)
if res >0:
    records=cursor.fetchall()
    for rec in records:
        print(rec['sname'])
    print(records)
cursor.close()
conn.close()