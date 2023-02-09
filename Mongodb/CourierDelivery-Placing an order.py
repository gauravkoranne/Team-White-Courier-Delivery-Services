import pymongo
import json
import pandas as pd
import time
# import datetime

client = pymongo.MongoClient("mongodb://localhost:27017/")

db = client["CourierDeliveryDB"]


db.drop_collection("Branch")
BranchCollection = db["Branch"]

db.drop_collection("Customer")
CustomerCollection = db["Customer"]

db.drop_collection("Staff")
StaffCollection = db["Staff"]

db.drop_collection("Shipment")
ShipmentCollection = db["Shipment"]

db.drop_collection("Payment")
PaymentCollection = db["Payment"]

csv_path = r"C:\Users\Mohammad\Documents\Desktop Files\Python Project\BigDataManagement\CSV Files\Branch.csv"
csv_data = pd.read_csv(csv_path)
payload = json.loads(csv_data.to_json(orient='records'))

db.Branch.insert_many(payload)
db.Branch.create_index([("BranchID",pymongo.ASCENDING)],unique=True)

csv_path = r"C:\Users\Mohammad\Documents\Desktop Files\Python Project\BigDataManagement\CSV Files\Customer.csv"
csv_data = pd.read_csv(csv_path)
payload = json.loads(csv_data.to_json(orient='records'))
db.Customer.create_index([("CustomerID",pymongo.ASCENDING)],unique=True)
db.Customer.insert_many(payload)


csv_path = r"C:\Users\Mohammad\Documents\Desktop Files\Python Project\BigDataManagement\CSV Files\Staff.csv"
csv_data = pd.read_csv(csv_path)
payload = json.loads(csv_data.to_json(orient='records'))
# db.Staff.create_index([("StaffID",pymongo.ASCENDING)],unique=True)
db.Staff.insert_many(payload)


csv_path = r"C:\Users\Mohammad\Documents\Desktop Files\Python Project\BigDataManagement\CSV Files\Shipment.csv"
csv_data = pd.read_csv(csv_path)
payload = json.loads(csv_data.to_json(orient='records'))
# db.Shipment.create_index([("OrderID",pymongo.ASCENDING)],unique=True)
db.Shipment.insert_many(payload)

csv_path = r"C:\Users\Mohammad\Documents\Desktop Files\Python Project\BigDataManagement\CSV Files\Payment.csv"
csv_data = pd.read_csv(csv_path)
payload = json.loads(csv_data.to_json(orient='records'))
# db.Payment.create_index([("TransactionID",pymongo.ASCENDING)],unique=True)
db.Payment.insert_many(payload)


# For testing data Just add another customer
db.Customer.insert_one({
    "CustomerID":1001
    ,"FullName":"Mohammadreza Yazdankhah"
    ,"Email":"yazdankhah@email.com"
    ,"PhoneNumber":"01791231234"
    ,"Address":"Heidelberg"
    ,"TotalConfirmedOrders":0
    })

CustomerName = input("Please type your full name: ")
CurrentCustomer = db.Customer.find({"FullName":CustomerName})
for item in CurrentCustomer:
    print("CustomerID = ",item['CustomerID'],"\n")
    print("Customer Full Name = ",str(item['FullName']),"\n")
    print("Customer Total Confirmed Orders = ",str(item['TotalConfirmedOrders']),"\n")
    print("=====================================================","\n")
CustomerID = input("Please enter your Customer ID:")
TotalConfirmedOrders = input("Please enter your total confirmed orders:")
print("Please select your Branch from the list in below: ","\n")
var = db.Branch.find().limit(2)
for item in var:
    print("BranchID = "+str(item['BranchID']),'\n')
    print("Branch Name = "+item['BranchName'],'\n')
    print("Address = "+item['Address'],'\n')
    print("Email = "+item['Email'],'\n')
    print("==============================================")

BranchID = input("Enter BranchID: ")
print("Now enter your package details:","\n")
weight=input("Enter the weight: ")
quantity = input("Enter the quantity: ")
deliveryaddress = input("Enter the delivery address: ") 

print("Select Payment Method:\n1. Visa\n2. Master\n ")
paymentMethod= input("Enter your choice:")
if paymentMethod == 1:
    method = "Visa"
else:
    method = "Master"
print("Please wait for transaction","\n")
time.sleep(2)

print("Payment confirmed")
print("Shipment confirmed")

Shipmentdoc={
 "Order_ID":int(CustomerID)*int(TotalConfirmedOrders)+2000
,"CustomerID":int(CustomerID)
,"BranchID":BranchID
,"ShipmentDate":time.strftime("%Y/%m/%d")
,"ShipmentTime":time.strftime("%H:%M:%S")
,"Weight":weight
,"Quantity":quantity
,"DeliveryAddress":deliveryaddress
,"TransactionID":int(CustomerID)*int(TotalConfirmedOrders)+2000
,"TrackingNumber":"123-3321-1231"
,"ShipmentStatus":"shipment confirmed"
,"ShipmentComments":""
}
db.Shipment.insert_one(Shipmentdoc)
trackingnumber = db.Shipment.find({"Order_ID":int(CustomerID)*int(TotalConfirmedOrders)+2000})
for item in trackingnumber:
    print("The Tracking Number is ",str(item['TrackingNumber']))

Paymentdoc = {
"TransactionID":int(CustomerID)*int(TotalConfirmedOrders)+2000
,"OrderID":int(CustomerID)*int(TotalConfirmedOrders)+2000
,"CustomerID":int(CustomerID)
,"PaymentMethod":method
}
db.Payment.insert_one(Paymentdoc)

db.Customer.update_one({"CustomerID":int(CustomerID)},{"$set":{"TotalConfirmedOrders":int(TotalConfirmedOrders)+1}})



