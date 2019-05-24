import pymysql
import  settings

conn=pymysql.Connect(**settings.parameters)
cursor=conn.cursor(cursor=pymysql.cursors.DictCursor)
sql="""
  create table if not exists user(uid int  auto_increment,username varchar(30) ,usertype enum ('管理员','普通用户') default'普通用户', 
  password char(100) not null,regtime datetime not null,email varchar(50) not null,primary key(uid,username))engine=innodb default charset=utf8;

"""
res=cursor.execute(sql)
if res >0:
    print("创建成功")
else:
    print("创建失败")
cursor.close()
conn.close()