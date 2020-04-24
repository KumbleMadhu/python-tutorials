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

# import pymongo
#
# client_abc = pymongo.MongoClient("mongodb+srv://Madhu:myiDB0000@learningmdb-en9um.gcp.mongodb.net/test?retryWrites=true&w=majority")
# mydb = client_abc["dbsample"]
# mycoll = mydb["customers"]
#
# for x in mycoll.find({},{"country": 1, "name": 1}):
#   print(x)

# MongoDB Query(for filtering the result while finding the docs) #
# import pymongo
# client_abc = pymongo.MongoClient("mongodb+srv://Madhu:myiDB0000@learningmdb-en9um.gcp.mongodb.net/test?retryWrites=true&w=majority")
# mydb = client_abc["dbsample"]
# mycoll = mydb["customers"]
#
# query = {"country": "Germany"}
# doc = mycoll.find(query)
# for i in doc:
#     print(i)

# # advanced query #
# import pymongo
# client_abc = pymongo.MongoClient("mongodb+srv://Madhu:myiDB0000@learningmdb-en9um.gcp.mongodb.net/test?retryWrites=true&w=majority")
# mydb = client_abc["dbsample"]
# mycoll = mydb["customers"]
#
# query = {"age": {"$gt": "22"}}
#
# doc = mycoll.find(query)
# for i in doc:
#     print(i)

# # Filter With Regular Expressions #
# import pymongo
# client_abc = pymongo.MongoClient("mongodb+srv://Madhu:myiDB0000@learningmdb-en9um.gcp.mongodb.net/test?retryWrites=true&w=majority")
# mydb = client_abc["dbsample"]
# mycoll = mydb["customers"]
#
# query = {"country": {"$regex": "^G"}}
#
# doc = mycoll.find(query)
# for i in doc:
#     print(i)

# # Sort the result #
# import pymongo
# client_abc = pymongo.MongoClient("mongodb+srv://Madhu:myiDB0000@learningmdb-en9um.gcp.mongodb.net/test?retryWrites=true&w=majority")
# mydb = client_abc["dbsample"]
# mycoll = mydb["customers"]
#
# doc = mycoll.find().sort("name")
# for i in doc:
#     print(i)

# # Sort descending #
# import pymongo
# client_abc = pymongo.MongoClient("mongodb+srv://Madhu:myiDB0000@learningmdb-en9um.gcp.mongodb.net/test?retryWrites=true&w=majority")
# mydb = client_abc["dbsample"]
# mycoll = mydb["customers"]
#
# doc = mycoll.find().sort("name", -1)
# for i in doc:
#     print(i)


# # Delete doc(one and many) #
# import pymongo
# client_abc = pymongo.MongoClient("mongodb+srv://Madhu:myiDB0000@learningmdb-en9um.gcp.mongodb.net/test?retryWrites=true&w=majority")
# mydb = client_abc["dbsample"]
# mycoll = mydb["customers"]
#
# querry = {"location": "India"}
# x = mycoll.delete_one(querry)
# print(x)
#
# querry = {"location": {"$regex": "^G"}}
# x = mycoll.delete_many(querry)
# print(x.deleted_count," documents deleted!")


# Deleting all the documents in a collection #
# import pymongo
# client_abc = pymongo.MongoClient("mongodb+srv://Madhu:myiDB0000@learningmdb-en9um.gcp.mongodb.net/test?retryWrites=true&w=majority")
# mydb = client_abc["dbsample"]
# mycoll = mydb["customers"]
#
# x =   mycoll.delete_many({})
# print(x.deleted_count, "docs deleted!")


# Deleting a collection(using drop() method) #
# import pymongo
#
# client_abc = pymongo.MongoClient("mongodb+srv://Madhu:myiDB0000@learningmdb-en9um.gcp.mongodb.net/test?retryWrites=true&w=majority")
# mydb = client_abc["dbsample"]
# mycoll = mydb["customers"]
#
# mycoll.drop()

# # updating many docs in a collection #
# import pymongo
# client_100 = pymongo.MongoClient("mongodb+srv://Madhu:myiDB0000@learningmdb-en9um.gcp.mongodb.net/test?retryWrites=true&w=majority")
# mydb = client_100["dbtest"]
# my_coll = mydb["USprj"]
#
# my_query = {"location": {"$regex": "^I"}}
# new_values = {"$set": {"name": "Krishna"}}
#
# x = my_coll.update_many(my_query, new_values)
# print(x.modified_count, "docs updated!")


# # Limiting the result #
# import pymongo
# client_100 = pymongo.MongoClient("mongodb+srv://Madhu:myiDB0000@learningmdb-en9um.gcp.mongodb.net/test?retryWrites=true&w=majority")
# mydb = client_100["dbtest"]
# my_coll = mydb["USprj"]
#
# result = my_coll.find().limit(2)
# for z in result:
#     print(z)