import  pymysql
import  settings
conn=pymysql.connect(**settings.parameters)
cursor=conn. cursor(cursor=pymysql.cursors.DictCursor)
sql='create database bbs default charset=utf8'
res=cursor.execute(sql)
if res >0:
    print("创建成功")
else:
    print("创建失败")
conn.close()
cursor.close()