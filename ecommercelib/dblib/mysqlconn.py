import pymysql


def createconn():
    conn = pymysql.connect(host="127.0.0.1", user="root", passwd="password", db="ecommercedb")
    return conn

