import pymongo

# Connect to the MongoDB client
client = pymongo.MongoClient("mongodb://localhost:27017/")
# Select the database and collection
db = client["Cancel_Orders"]
orders = db["Orders"]
# Find the order to cancel using its ID
order_id =input("Enter your order_id")

order = orders.find_one({"order_id": order_id})
# Update the order status to "cancelled"
#order["status"] = "cancelled"
#print(order)
a = {"order_id":order_id}
print(order)
b = {"$set":{"order_status":"Cancel"}}
#cfg= orders.update_one(a,b)


#for i in order_status:
    #print("order_status"+ order_status)

#result = orders.update_one({"id": order_id}, {"$set": order})
# Check if the update was successful
#if result.modified_count > 0:
#    print("Order successfully cancelled!")
#else:
#    print("Could not cancel the order. Please try again.")


"""db = client["Cancel_orders"]
orders = db["orders"]
"""

pipeline= orders.aggregate(
    [
        {
            "$match": {"order_id":order_id}
        },
        {
            "$project": {"email":1,"order_status":1, "order_id":1,"Address":1}
        },
        {
            "$limit":50
        }
    ]
)



"""order_id = "3948"
order = orders.find_one({"id": order_id})
a = {"id":order_id}
b = {"$set":{"order_status":"cancelled"}}"""
for items in pipeline:
    if items['order_status']=="Delivered":
        print("Order delivered cannot be cancelled")
    elif items['order_status']=="Warehouse":
        items['order_status']=orders.update_one(a,b)
        print(items['order_status'])

    elif items['order_status']=="Transit ":
        items['order_status']=orders.update_one(a,b)
        print(items['order_status'])  

    elif items['order_status']=="Postpone":
        items['order_status']=orders.update_one(a,b)
        print(items['order_status']) 
    
    elif items['order_status']=="Wrong_Address":
        address= input("Enter your addr")
        if address!=items['Address']:
            items['order_status']=orders.update_one(a,b)
            print(items['order_status']) 
            print("Your address did not match with database order cancelled")

    # if 'Address' in items and items['order_status'] == "Wrong_Address":
    #     address = input("Enter your address: ")
    #     if address != items['Address']:
    #         items['order_status'] = orders.update_one(a, b)
    #         print(items['order_status'])
    #     else:
    #         print("Error: The Address key does not exist in the items dictionary or the order status is not 'Wrong_Address'")


    #else:
        #print("Order cancelled successfully")



#orders.update_one(a,b)
#print(items)

