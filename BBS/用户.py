import  hashlib
import  pymysql
import settings
conn=pymysql.connect(**settings.parameters)
cursor=conn.cursor(cursor=pymysql.cursors.DictCursor)
while 1:
 username=input("请输入用户名：")
 password=input("请输入密码：")
 password = hashlib.sha1(password.encode('utf8')).hexdigest()
 sql = "select username,password from user where username=%s and password=%s"
 res = cursor.execute(sql,[username,password])

 if res > 0:
    print("登录成功")
    sql="""
        select username ,usertype, password, email from user where username='%s'
    """%username
    res = cursor.execute(sql)
    a=cursor.fetchall()
    print()
    print(a)
 elif res< 0:
    print("登陆失败")
    continue


conn.close()
cursor.close()