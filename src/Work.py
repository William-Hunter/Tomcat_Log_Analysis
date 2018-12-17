# coding=utf-8
import os
import time
import glob
import mysql_connector
# import PyMy

print "运行开始"

SERVER_ONE='47.47.47.47'
SERVER_TWO='47.47.47.47'

def insertdb(values,tomcat_ip):
    cursor = db.cursor()
    current_time=time.strftime("%Y-%m-%d %H:%M:%S", time.strptime(values[2].replace("[",""), "%d/%b/%Y:%H:%M:%S"))
    sql = "INSERT INTO localhost_access_log(`ip`,`time`,`method`,`url`,`state_code`,`length`,`process_mils`,`response_mils`,`tomcat_ip`)"
    sql=sql+" VALUES (\'"+values[0]+"\',\'"+current_time+"\',\'"+values[4].replace("\"","")+"\',\'"+values[5]+"\',\'"+values[7]+"\',\'"+values[8]+"\',\'"+values[9]+"\',\'"+values[10]+"\',\'"+tomcat_ip+"\')"
    print sql
    try:
        cursor.execute(sql)
        db.commit()
        print "日志插入成功！"
    except Exception, e:
        print "插入失败"
        print e
        db.rollback()

def readFile(file_path,tomcat_ip):
    file =open(file_path)
    line = file.readline()
    while line:
        values=line.split(" ")
        insertdb(values,tomcat_ip)
        line = file.readline()

#localtime=time.strftime("%Y-%m-%d",time.localtime())

# db=PyMy.connectdb()
db= mysql_connector.connectdb()
if db is not None:
    file_list = glob.glob(r"../material/mem/localhost_access_log.*.txt")
    for filename in file_list:
        readFile(filename, SERVER_ONE)
        os.remove(filename)
    file_list = glob.glob(r"../material/tckj/localhost_access_log.*.txt")
    for filename in file_list:
        readFile(filename, SERVER_TWO)
        os.remove(filename)
    db.close()
print "运行结束"

