import pymysql
import  settings
import  datetime
import hashlib
conn=pymysql.Connect(**settings.parameters)
cursor=conn.cursor(cursor=pymysql.cursors.DictCursor)
while 1:
 username=input("请输入用户名：")
 sql="""
   select username from user where username=%s
 """%username
 res=cursor.execute(sql)
 if res>0:
     username=input('用户名已存在，请重新输入：')

 if len(username) <= 2 or username.isspace():
     username = input("请重新输入用户名：")
     continue
 else:
    break
password=input("请输入密码：")
password=hashlib.sha1(password.encode('utf8')).hexdigest()
email=input("请输入你的邮箱：")
nowTime=datetime.datetime.now()
a=nowTime
sql="""
    insert into user(username,password,regtime,email) values('%s','%s','%s','%s')
"""%(username,password,a,email)
print(sql)
try:
    res=cursor.execute(sql)
    if res:
        conn.commit()
    else:
        conn.rollback()
except Exception as  e:
    print(e)
    conn.rollback()
finally:
    cursor.close()
    conn.close()