import sqlite3

import mysql.connector
#
#
def createconn():
    conn = mysql.connector.connect(host="localhost",
                                   user='root',
                                   password='vignesh',
                                   database='bankingdb',
                                   auth_plugin='mysql_native_password')

    c = conn.cursor()
    return c, conn


createconn()


class MetaSingleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(MetaSingleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class Database(metaclass=MetaSingleton):
    connection = None

    def connect(self):
        if self.connection is None:
            self.connection = sqlite3.connect("db.sqlite3")
            self.cursorobj = self.connection.cursor()
        return self.cursorobj


db1 = Database().connect()
db2 = Database().connect()
print("Database Objects DB1", db1)
print("Database Objects DB2", db2)
