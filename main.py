import mysql.connector
import pymongo
from mongo_utilize import create_mongo_db, connect_mongo_db
from mysql_utilize import create_mysql_db, connect_mysql_db, connect_mysql
import insert_list_product_data, insert_list_product_type_data, insert_list_image_data
from redis_db import RedisDB
from sample_cart import sample_carts


def execute_schema(file_path):
    # init schema
    with open(file_path) as f:
        command = f.read().replace('\n', "").replace('\t', "")
    command = command.split(';')
    for c in command:
        if c != "":
            try:
                print("command:", c)
                mysqlcursor.execute(c+";")
                print("-------")
            except Exception as e:
                print("Error: ", e)


if __name__ == "__main__":

    """ 
        THIS IS USER && PAYMENT SECTION. USE MYSQL
        IT INCLUDE: CONNECT MYSQL, CREATE MYSQL DB, CONNECT MYSQL DB, CREATE SCHEMA BY QUERY, INSERT DATA BY QUERY
    """

    myconn = connect_mysql(host="localhost", username="root", password="")
    # create mysql db
    create_mysql_db(myconn, name_db = "TEAM")
    myconn.close()

    # connect to mysql db
    mysqldb = connect_mysql_db(host="localhost", username="root", password="", database="TEAM")
    

    mysqlcursor = mysqldb.cursor()

    # connect to mysql db
    # mysqldb = mysql.connector.connect(
    #     host="remotemysql.com",
    #     username="oFKYiTMu3e",
    #     password="U0yUKMhIQz",
    #     database="oFKYiTMu3e")

    # mysqlcursor = mysqldb.cursor()

    #execute_schema("schema.sql")
    execute_schema("userSchema.sql")
    execute_schema("orderSchema.sql")
    execute_schema("paymentSchema.sql")
    execute_schema("insert_user.sql")
    execute_schema("insert_orders.sql")
    execute_schema("insert_payment.sql")

    mysqldb.commit()
    # insert data into taxon
    # execute_schema("insert_data_taxon.sql")

    # insert data into product
    # execute_schema("insert_data_product.sql")
    mysqldb.commit()

    """ 
        THIS IS PRODUCT SECTION. USE MONGODB
        IT INCLUDE: CONNECT MONGO, CREATE & CONNECT MONGO DB, CREATE COLLECTION, INSERT DATA
    """

    # connect to mongo db
    # connect and create mongo db
    mongoclient = connect_mongo_db(MONGO_URI="mongodb://localhost:27017")

    mongo_mydb = create_mongo_db(mongoclient)

    # create collection
    mongo_mycol = mongo_mydb["Product"]

    # insert data in product collection
    list_product = insert_list_product_data.list_product
    x = mongo_mycol.insert_many(list_product)

    # create collection
    mongo_mycol = mongo_mydb["Product_type"]

    # insert data in product collection
    list_product_type = insert_list_product_type_data.list_product_type
    x = mongo_mycol.insert_many(list_product_type)

    # create collection
    mongo_mycol = mongo_mydb["Image"]

    # insert data in product collection
    list_image = insert_list_image_data.list_image
    x = mongo_mycol.insert_many(list_image)

    print("Show all product types have product type name = snack Oshi:")
    myquery = {"product_type_name" : "snackOshi"}

    mydoc = mongo_mydb["Product_type"].find(myquery)

    for x in mydoc:
        print(x)
    # user click on a category
    # clicked_id = int(input("Enter category id (taxon id):"))

    # # get all products that belong to this category
    # print("Pick product from TEAM_PRODUCT with taxon_id:")
    # mysqlcursor.execute(
    #     "select * from TEAM_PRODUCT where taxon_id = {0}".format(clicked_id))
    # result = mysqlcursor.fetchall()
    # for row in result:
    #     print(row)


    """ 
        THIS IS CART SECTION. USE RedisDB
        IT INCLUDE: CREATE & CONNECT RedisDB, CREATE COLLECTION, INSERT DATA, SOME QUERY
    """

    redisDB = RedisDB()

    # insert cart of user 1 to redis db
    user1Id = 1
    redisDB.saveCart(user1Id, sample_carts[user1Id])

    # insert cart of user 2 to redis db
    user2Id = 2
    redisDB.saveCart(user2Id, sample_carts[user2Id])

    # show cart of user 1 to redis db
    print("Cart of user {}".format(user1Id))
    print(redisDB.getCart(user1Id))

    # show cart of user 2 to redis db
    print("Cart of user {}".format(user2Id))
    print(redisDB.getCart(user2Id))

    execute_schema("insert_order_related.sql")
    mysqldb.commit()
    # close connection to mysql db
    mysqldb.close()

    # close connection to mongo db
    mongoclient.close()
