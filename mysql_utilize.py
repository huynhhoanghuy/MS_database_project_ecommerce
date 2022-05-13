import mysql.connector
import pymongo

def connect_mysql(host="localhost", username="root", password="hoangHuy0206"):
    try:
        myconn = mysql.connector.connect(
                host="localhost",
                username="root",
                password="hoangHuy0206")
        return myconn
    except:
        print("CAN'T CONNECT MYSQL")

def connect_mysql_db(host="localhost", username="root", password="hoangHuy0206", database="TEAM"):
    try:
        mysqldb = mysql.connector.connect(
                host="localhost",
                username="root",
                password="hoangHuy0206",
                database="TEAM")
        return mysqldb
    except:
        print("CAN'T CONNECT MYSQL DB")
    
def create_mysql_db(myconn, name_db = "TEAM"):
    try:
        print("CREATE DATABASE "+ name_db)
        cur = myconn.cursor()
        cur.execute("create database "+ name_db)
        dbs = cur.execute("show databases")
        for x in cur:
            print(x)
    except:
        print("CAN'T CREATE MYSQL DB")
        myconn.rollback()
    
    