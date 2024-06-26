import sqlite3

import mysql.connector


#
#
def createconn():
    conn = mysql.connector.connect(host="127.0.0.1", port=3308,
                                   user='root',
                                   password='password',
                                   database='ecommercedb',
                                   auth_plugin='mysql_native_password')

    c = conn.cursor()
    return c, conn


class MetaSingleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(MetaSingleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class Database(metaclass=MetaSingleton):
    connection = None
    cursor = None

    def connect(self):
        if self.connection is None:
            self.cursor, self.connection = createconn()
            print (self.connection)
            # creating database
            #self.cursor.execute("CREATE DATABASE testdb")
        return self.cursor


db1 = Database().connect()
db2 = Database().connect()
print("Database Objects DB1", db1)
print("Database Objects DB2", db2)
