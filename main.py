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

    
    # connect and create mongo db
    mongoclient = connect_mongo_db(MONGO_URI = "mongodb://localhost:27017")
    
    mongo_mydb = create_mongo_db(mongoclient)
    
    #create collection
    mongo_mycol = mongo_mydb["Product"]

    #insert data in product collection
    list_product = insert_list_product_data.list_product
    x = mongo_mycol.insert_many(list_product)

    #create collection
    mongo_mycol = mongo_mydb["Product_type"]

    #insert data in product collection
    list_product_type = insert_list_product_type_data.list_product_type
    x = mongo_mycol.insert_many(list_product_type)

    #create collection
    mongo_mycol = mongo_mydb["Image"]

    #insert data in product collection
    list_image = insert_list_image_data.list_image
    x = mongo_mycol.insert_many(list_image)



    # # user click on a category
    # clicked_id = int(input("Enter category id (taxon id):"))

    # # get all products that belong to this category
    # print("Pick product from TEAM_PRODUCT with taxon_id:")
    # mysqlcursor.execute(
    #         "select * from TEAM_PRODUCT where taxon_id = {0}".format(clicked_id))
    # result = mysqlcursor.fetchall()
    # for row in result:
    #     print(row)

    #init user schema
    with open("userSchema.sql") as f:
        command = f.read().replace('\n',"").replace('\t',"")
    command = command.split(';')
    for c in command:
        if c != "":
            print("command:",c)
            mysqlcursor.execute(c+";")
            print("-------")
    result = mysqlcursor.fetchall()

    #init payment schema
    with open("paymentSchema.sql") as f:
        command = f.read().replace('\n',"").replace('\t',"")
    command = command.split(';')
    for c in command:
        if c != "":
            print("command:",c)
            mysqlcursor.execute(c+";")
            print("-------")
    result = mysqlcursor.fetchall()

    #insert data into user
    with open("insert_user.sql") as f:
        command = f.read().replace('\n',"").replace('\t',"")
    command = command.split(';')
    for c in command:
        if c != "":
            print("command:",c)
            mysqlcursor.execute(c+";")
            print("-------")
    result = mysqlcursor.fetchall()
    
    # user click on a category
    clicked_id = int(input("Enter category id (taxon id):"))
    
    # get all products that belong to this category
    print("Show Info user from USER_INFO with user_id:")
    mysqlcursor.execute(
            "select * from PAYMENT where user_id = '1'".format(clicked_id))
    result = mysqlcursor.fetchall()
    for row in result:
        print(row)

    # close connection to mysql db
    mysqldb.close()

    # close connection to mongo db
    mongoclient.close()

