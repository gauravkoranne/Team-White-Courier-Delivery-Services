# Import the PyMongo library
from time import strftime
import pymongo
import datetime

# Connect to the database
client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["CourierDeliveryDB"]
collection = db["userOrders"]
collection2 = db['paymentDetails']
print("Connection successful")
# Query the database
result = collection.find()

#insert into userOrders collection
userlist =[

{"userID" : "1", "firstName" : "Shwetanjali", "lastName" :"Zarekar", "email": "shwetazarekar6@gmail.com","courier":"Packages",
"price":"624.17","quantity":"7","paymentStatus":"Awaiting","shippingAddress":"259 Sutteridge Avenue"},

{"userID" : "2", "firstName" : "Andrew", "lastName" :"Leathley", "email": "aleathley1@qq.com","courier":"Packages",
"price":"643.53","quantity":"6","paymentStatus":"Awaiting","shippingAddress":"73246 Washington Parkway"},

{"userID" : "3", "firstName" : "Celeste", "lastName" :"Gilbody", "email": "celeste@gmail.com","courier":"Packages",
"price":"777.17","quantity":"4","paymentStatus":"Awaiting","shippingAddress":"701 Northport Park"},

{"userID" : "4", "firstName" : "Ardyce", "lastName" :"Phebey", "email": "Ardyce@gmail.com","courier":"Toys",
"price":"589.20","quantity":"7","paymentStatus":"Awaiting","shippingAddress":"86301 Larry Plaza"},

{"userID" : "5", "firstName" : "Wilbur", "lastName" :"Pebworth", "email": "Wilbur@gmail.com","courier":"Jewelry",
"price":"1000.10","quantity":"2","paymentStatus":"Awaiting","shippingAddress":"481 Hallows Way"},

{"userID" : "6", "firstName" : "Ashleigh", "lastName" :"Cheyne", "email": "Ashleigh6@gmail.com","courier":"Beauty",
"price":"800.30","quantity":"3","paymentStatus":"Awaiting","shippingAddress":"8904 Dahle Center"},

{"userID" : "7", "firstName" : "Marje", "lastName" :"Carnell", "email": "Marje@gmail.com","courier":"Clothing",
"price":"550.15","quantity":"10","paymentStatus":"Awaiting","shippingAddress":"1010 Prairieview Crossing"},

{"userID" : "8", "firstName" : "Olympe", "lastName" :"Tipling", "email": "tipling@gmail.com","courier":"Packages",
"price":"400.17","quantity":"6","paymentStatus":"Awaiting","shippingAddress":"09247 Northwestern Center"},

{"userID" : "9", "firstName" : "Sara", "lastName" :"Hazeltine", "email": "sarah@gmail.com","courier":"Packages",
"price":"720.20","quantity":"8","paymentStatus":"Awaiting","shippingAddress":"94947 Carey Hill"},

{"userID" : "10", "firstName" : "Selig", "lastName" :"Wigin", "email": "seligw@gmail.com","courier":"Packages",
"price":"980.50","quantity":"15","paymentStatus":"Awaiting","shippingAddress":"0 Florence Pass"},

{"userID" : "11", "firstName" : "Noah", "lastName" :"Walt", "email": "Noahw@gmail.com","courier":"Electronics",
"price":"1500.00","quantity":"2","paymentStatus":"Awaiting","shippingAddress":"03628 Schmedeman Junction"},

{"userID" : "12", "firstName" : "Mace", "lastName" :"Winston", "email": "macew@gmail.com","courier":"Packages",
"price":"851.59","quantity":"3","paymentStatus":"Awaiting","shippingAddress":"66316 Old Shore Park"},

{"userID" : "13", "firstName" : "Stanford", "lastName" :"Scotcher", "email": "stanford@gmail.com","courier":"Clothing",
"price":"768.71","quantity":"5","paymentStatus":"Awaiting","shippingAddress":"7670 Petterle Junction"},

{"userID" : "14", "firstName" : "Doris", "lastName" :"Wikey", "email": "doris@gmail.com","courier":"Packages",
"price":"678.07","quantity":"8","paymentStatus":"Awaiting","shippingAddress":"71 Dawn Alley"},

{"userID" : "15", "firstName" : "Brandtr", "lastName" :"Gainsborough", "email": "brandtr@gmail.com","courier":"Packages",
"price":"868.25","quantity":"6","paymentStatus":"Awaiting","shippingAddress":"490 Macpherson Point"},

{"userID" : "16", "firstName" : "Krystalle", "lastName" :"Warack", "email": "krystalle@gmail.com","courier":"Electronics",
"price":"624.17","quantity":"7","paymentStatus":"Awaiting","shippingAddress":"5930 Mosinee Park"},

{"userID" : "17", "firstName" : "Wenonah", "lastName" :"Lukianovich", "email": "Lukianovich@gmail.com","courier":"Packages",
"price":"755.13","quantity":"3","paymentStatus":"Awaiting","shippingAddress":"74 Sloan Plaza"},

{"userID" : "18", "firstName" : "Analiese", "lastName" :"Gristock", "email": "Gristock@gmail.com","courier":"Packages",
"price":"884.26","quantity":"12","paymentStatus":"Awaiting","shippingAddress":"68617 Sauthoff Circle"},

{"userID" : "19", "firstName" : "Davine", "lastName" :"Gilham", "email": "Gilham@gmail.com","courier":"Electronics",
"price":"725.30","quantity":"7","paymentStatus":"Awaiting","shippingAddress":"259 Sutteridge Avenue"},

{"userID" : "20", "firstName" : "Max", "lastName" :"Muller", "email": "max36@gmail.com","courier":"Packages",
"price":"560.60","quantity":"4","paymentStatus":"Awaiting","shippingAddress":"359 Sutteridge Avenue"},

]

db.userOrders.insert_many(userlist)


# Loop through the results and display them on the page
#print("Order Summary: ")
#for info in result:
    
 #   print("Customer ID:" + info['userID'])
 #   print("First Name:"+  info['firstName'])
 #   print("Last Name:" + info['lastName'])
  #  print("Shipping Address:" + info['shippingAddress'])
  #  print("Courier:" + info['courier'])
  #  print("Quantity:" + info['quantity'])
    #print("Price:" + info['price'])
   # total = round((float(info['quantity']) * float(info['price'])),2)
   # print("Subtotal is :" + str(total))
   # print("Payment Status: " + info['paymentStatus'] + "\n")
    
   # Find all documents in the collection and store the desired field in an array


selecteduser = input("Enter your User ID: ")

var1 =  db.userOrders.find( { "userID" : selecteduser } )
#print(var1)
for x in var1:
    print("First Name: "+x['firstName'])
    print("Last Name: " +x['lastName'])
    print("Courier: " +x['courier'])
    print("Price: " +x['price'])
    print("Quantity: " +x['quantity'])
    print("Payment Status " +x['paymentStatus'])
    print("Shipping Address: " +x['shippingAddress'])
    total = round((float(x['quantity']) * float(x['price'])),2)
    print("Subtotal:"+ str(total)+"\n")
    break
print("Select Payment Method:\n1. Credit Card\n2. Debit Card\n ")
paymentMethod= input("Enter your choice:")

if paymentMethod == "1":
        cardnumber = input("Enter Card Number: ")
        expiryYear = input("Enter Card Expiry Year: ")
        cvv = input("Enter CVV Number: ")
        otp = input("Enter OTP: ")
        status = "successful"

elif paymentMethod == "2":
        cardnumber = input("Enter Card Number: ")
        expiryYear = input("Enter Card Expiry Year: ")
        cvv = input("Enter CVV Number: ")
        otp = input("Enter OTP: ")
        status = "successful"

else:
        print("Invalid option. Please try again.")

document = {"userID": selecteduser,"cardNumber":cardnumber,"expiryYear":expiryYear,"paymentMethod":paymentMethod, 
            "amount":str(total),"paymentStatus":status,"TimeStamp":datetime.datetime.now()}
collection2.insert_one(document)

# Define the filter to find the document to update
filter = {"userID": selecteduser}

# update operation
update = {"$set": {"paymentStatus": "successful"}}

# Update the document in the collection
collection.update_one(filter, update)

print("Payment Successful !!\n")
print("*Order confirmed*\n")
print("First Name: "+x['firstName'])
print("Last Name: " +x['lastName'])
print("Courier: " +x['courier'])
print("Price: " +x['price'])
print("Quantity: " +x['quantity'])
print("Payment Status " +str(update))
print("Subtotal: "+str(total))
print("Shipping Address: " +x['shippingAddress'] )
print("TimeStamp:"+ str(datetime.datetime.now())+"\n")


