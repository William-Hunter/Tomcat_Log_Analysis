# coding=utf-8

import mysql.connector
import DataBaseConfig

def connectdb():
    print('正在连接到mysql服务器...')
    try:
        db = mysql.connector.connect(**DataBaseConfig._254)
        print('连接上了!')
        return db
    except Exception, e:
        print "数据库连接失败"
        print e


