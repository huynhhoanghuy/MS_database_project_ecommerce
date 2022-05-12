import mysql.connector
import pymongo

if __name__ == "__main__":

    

    myconn = mysql.connector.connect(
    host="localhost",
    username="root",
    password="hoangHuy0206")

    # tạo đối tượng cursor
    cur = myconn.cursor()

    try:
        cur.execute("create database TEAM")
        dbs = cur.execute("show databases")
        for x in cur:
            print(x)
    except:
        myconn.rollback()
    
    myconn.close()

    # connect to mysql db
    mysqldb = mysql.connector.connect(
    host="localhost",
    username="root",
    password="hoangHuy0206",
    database="TEAM")

    mysqlcursor = mysqldb.cursor()

    #init schema
    with open("schema.sql") as f:
        command = f.read().replace('\n',"").replace('\t',"")
    command = command.split(';')
    for c in command:
        if c != "":
            print("command:",c)
            mysqlcursor.execute(c+";")
            print("-------")
    result = mysqlcursor.fetchall()
    
    #insert data into taxon
    with open("insert_data_taxon.sql") as f:
        command = f.read().replace('\n',"").replace('\t',"")
    command = command.split(';')
    for c in command:
        if c != "":
            print("command:",c)
            mysqlcursor.execute(c+";")
            print("-------")
    result = mysqlcursor.fetchall()

    #insert data into product
    with open("insert_data_product.sql") as f:
        command = f.read().replace('\n',"").replace('\t',"")
    command = command.split(';')
    for c in command:
        if c != "":
            print("command:",c)
            mysqlcursor.execute(c+";")
            print("-------")
    result = mysqlcursor.fetchall()

    
    # connect to mongo db
    mongoclient = pymongo.MongoClient("mongodb://localhost:27017/")


    # user click on a category
    clicked_id = int(input("Enter category id (taxon id):"))

    # get all products that belong to this category
    print("Pick product from TEAM_PRODUCT with taxon_id:")
    mysqlcursor.execute(
            "select * from TEAM_PRODUCT where taxon_id = {0}".format(clicked_id))
    result = mysqlcursor.fetchall()
    for row in result:
        print(row)

    #init schema
    with open("userSchema.sql") as f:
        command = f.read().replace('\n',"").replace('\t',"")
    command = command.split(';')
    for c in command:
        if c != "":
            print("command:",c)
            mysqlcursor.execute(c+";")
            print("-------")
    result = mysqlcursor.fetchall()

    # close connection to mysql db
    mysqldb.close()

    # close connection to mongo db
    mongoclient.close()

