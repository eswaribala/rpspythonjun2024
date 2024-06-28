# -*- coding: utf-8 -*-
"""
Created on Thu Jan  4 15:09:38 2018

@author: Balasubramaniam
"""

import pymysql


def createConnection():
    conn = pymysql.connect(host="localhost", user="root",
                           passwd="vignesh",
                           db="bankingdb")
    return conn;


#createConnection()

'''

def fetchBytestCaseId(id):
    conn=createConnection()
    cursor=conn.cursor()
    cursor.execute("""select * from testcaseresults where 
    tcno='%d'""" %(id))
    return cursor.fetchall()


def addTestCaseInfo(data):
    connObj=createConnection();
    cursor=connObj.cursor();
    print("Cursor ready...");     
    try:
        cursor.execute("""insert into testcaseresults values 
    ('%d','%s','%d')""" %(data[0],data[1],data[2]));
        #cursor.execute(query);
        connObj.commit()
    except pymysql.Error as e:
        print("Exception occurred",e )
        connObj.rollback()

    finally:
        connObj.close()
    
#tsData=[1099,'REQ1099',1];
#addTestCaseInfo(tsData);
rows = fetchBytestCaseId(1002);

for row in rows:
    print(row);

'''
