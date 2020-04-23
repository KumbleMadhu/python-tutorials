## creating a database ##
# import pymongo
#
# client_abc = pymongo.MongoClient("mongodb+srv://Madhu:myiDB0000@learningmdb-en9um.gcp.mongodb.net/test?retryWrites=true&w=majority")
# mydb = client_abc["dbsample"]
#
# print(client_abc.list_database_names())     # to check if a database exist by listing all databases in your system #
#
# dblist = client_abc.list_database_names()
# if "dbsample"in dblist:
#     print("The database exists!")

# Creating collection called customers(like table) #
# import pymongo
# client_abc = p    ymongo.MongoClient("mongodb+srv://Madhu:myiDB0000@learningmdb-en9um.gcp.mongodb.net/test?retryWrites=true&w=majority")
# mydb = client_abc["dbsample"]
# mycoll = mydb["customers"]

# print(mydb.list_collection_names())
# coll_list = mydb.list_collection_names()
# if "customers" in coll_list:
#     print("The collection exists!")

## Inserting Document/record into collection ##
# import pymongo
#
# client_abc = pymongo.MongoClient("mongodb+srv://Madhu:myiDB0000@learningmdb-en9um.gcp.mongodb.net/test?retryWrites=true&w=majority")
# mydb = client_abc["dbsample"]
# mycoll = mydb["customers"]
#
# mydict = {"Name": "Madhu", "age": "22", "country": "India"}
#
# x = mycoll.insert_one(mydict)
# print(x.inserted_id)

## Inserting multiple documents into a collection ##

# import pymongo
# client_abc = pymongo.MongoClient("mongodb+srv://Madhu:myiDB0000@learningmdb-en9um.gcp.mongodb.net/test?retryWrites=true&w=majority")
# mydb = client_abc["dbsample"]
# mycoll = mydb["customers"]
#
# mylist = [
#     {"Name": "Madhu", "age": "22", "country": "India"},
#     {"Name": "Akash", "age": "54", "country": "Germany"},
#     {"Name": "Tim", "age": "32", "country": "Spain"},
#     {"Name": "John", "age": "12", "country": "NY"},
#     {"Name": "David", "age": "27", "country": "Netherlands"}
#         ]
# x = mycoll.insert_many(mylist)
# print(x.inserted_ids)   # which is assigning the unique IDs everytime #
#

## Specified IDs ##
# import pymongo
# client_abc = pymongo.MongoClient("mongodb+srv://Madhu:myiDB0000@learningmdb-en9um.gcp.mongodb.net/test?retryWrites=true&w=majority")
# mydb = client_abc["dbsample"]
# mycoll = mydb["customers"]
#
# mylist = [
#     {"_id": 1, "Name": "Madhu", "age": "22", "country": "India"},
#     {"_id": 2, "Name": "Akash", "age": "54", "country": "Germany"},
#     {"_id": 3, "Name": "Tim", "age": "32", "country": "Spain"},
#     {"_id": 4, "Name": "John", "age": "12", "country": "NY"},
#     {"_id": 5, "Name": "David", "age": "27", "country": "Netherlands"}
#         ]
# x = mycoll.insert_many(mylist)
# print(x.inserted_ids)

## Find/get(first doc) data in a collection ##
# import pymongo
# client_abc = pymongo.MongoClient("mongodb+srv://Madhu:myiDB0000@learningmdb-en9um.gcp.mongodb.net/test?retryWrites=true&w=majority")
# mydb = client_abc["dbsample"]
# mycoll = mydb["customers"]
#
# x = mycoll.find_one()
# print(x)

# import pymongo  # Returning all the docs and printing them!
#
# client_abc = pymongo.MongoClient("mongodb+srv://Madhu:myiDB0000@learningmdb-en9um.gcp.mongodb.net/test?retryWrites=true&w=majority")
# mydb = client_abc["dbsample"]
# mycoll = mydb["customers"]
#
# for v in mycoll.find():
#     print(v)


# return particular fields
# import pymongo
#
# client_abc = pymongo.MongoClient("mongodb+srv://Madhu:myiDB0000@learningmdb-en9um.gcp.mongodb.net/test?retryWrites=true&w=majority")
# mydb = client_abc["dbsample"]
# mycoll = mydb["customers"]
#
# for v in mycoll.find({}, {"_id": 0, "name": 1, "age": 1}):
#   print(v)

import pymongo

client_abc = pymongo.MongoClient("mongodb+srv://Madhu:myiDB0000@learningmdb-en9um.gcp.mongodb.net/test?retryWrites=true&w=majority")
mydb = client_abc["dbsample"]
mycoll = mydb["customers"]

for x in mycoll.find({},{"country": 1, "name": 1}):
  print(x)