# connect to your Mongo DB database

# the changes to commit here i will create a new file for connection with MOnoDB Database 
from pymongo import MongoClient


client = MongoClient("mongodb+srv://b21124:f8Yuo2hEHui6YC3i@cluster0.2kag3bh.mongodb.net/?retryWrites=true&w=majority")
db = client.get_database('total_records')
records = db.register

db1 = client.get_database('AddedItems')
addItems = db1.register

db3 = client.get_database('customers')
records1 = db3.register

db2 = client.get_database('Finance')
collectPayment = db2.CollectPayment
Pay = db2.pay