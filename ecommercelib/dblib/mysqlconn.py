import sqlite3

import pymysql


class Database():
    connection = None
    def connect(self):
        if self.connection is None:
            self.connection = sqlite3.connect("db.sqlite3")
            self.cursorobj = self.connection.cursor()
        return self.cursorobj
db1 = Database().connect()
db2 = Database().connect()
print ("Database Objects DB1", db1)
print ("Database Objects DB2", db2)
