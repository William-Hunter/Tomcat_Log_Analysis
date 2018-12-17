#!/usr/bin/env python
# coding=utf-8

# import pymysql
import DataBaseConfig


def connectdb():
    print('连接到mysql服务器...')
    db = pymysql.connect(**DataBaseConfig.config)
    print('连接上了!')
    return db