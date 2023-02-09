import redis
# Connect to the Redis database
redis = redis.Redis(
    host='localhost',
    port='6379')
# Prompt the user to select a key option to find the distance between
print("Please Choose a key option to find distance between as 1, 2, 3, 4, 5, from : \n 1. PickUp to driver  \n 2. PickUp to parcel_shop \n 3. Driver to parcel_shop \n 4. parcel_shop to Delivery \n 5. Driver to Delivery")
i = input("Enter - ")
i = int(i)
# Check the user's input and perform the relevant action
if i == 1:
    # Combining two keys into a temporary key called Temp
    redis.zunionstore("Temp", ("PickUp", "Driver"), aggregate="MIN")

    # Expiring Temporary created key
    redis.expire("Temp", 300)

    PickUp = input("Enter  PickUp name: ")
    Driver = input("Enter Driver name: ")

    # Find the distance between the PickUp and Driver names
    Distance = redis.geodist("Temp", PickUp,Driver, unit="km")

    
    if Distance == None:
        print("Enter correct details since you have entered wrong details")
    else:
        print(" Distance: ", Distance,"km")

elif i == 2:
    # Combining two keys
    redis.zunionstore("Temp", ("PickUp", "parcel_shop"), aggregate="MIN")

    
    redis.expire("Temp", 300)

    parcel_shop = input("Enter parcel_shop name: ")
    PickUp = input("Enter  PickUp name: ")

    Distance = redis.geodist("Temp", parcel_shop,PickUp, unit="km")

    if Distance == None:
        print("Enter correct details since you have entered wrong details")
    else:
        print(" Distance: ", Distance,"km")

elif i == 3:
    # Combining two keys
    redis.zunionstore("Temp", ("Driver", "parcel_shop"), aggregate="MIN")

    
    redis.expire("Temp", 300)

    parcel_shop = input("Enter parcel_shop: ")
    Driver = input("Enter Driver name: ")

    Distance = redis.geodist("Temp", Driver, parcel_shop, unit="km")

    if Distance == None:
        print("Enter correct details since you have entered wrong details")
    else:
        print(" Distance: ", Distance,"km")
elif i == 4:
    # Combining two keys
    redis.zunionstore("Temp", ("Delivery", "parcel_shop"), aggregate="MIN")

    
    redis.expire("Temp", 300)

    Delivery = input("Enter Delivery name: ")
    parcel_shop = input("Enter parcel_shop name: ")

    Distance = redis.geodist("Temp", parcel_shop, Delivery, unit="km")

    if Distance == None:
        print("Enter correct details since you have entered wrong details")
    else:
        print(" Distance: ", Distance,"km")
      
elif i == 5:
    
    redis.zunionstore("Temp", ("Delivery", "Driver"), aggregate="MIN")

    
    redis.expire("Temp", 300)

    Delivery = input("Enter Delivery name: ")
    Driver = input("Enter Driver name: ")

    Distance = redis.geodist("Temp", Driver, Delivery, unit="km")

    if Distance == None:
        print("Enter correct details since you have entered wrong details")
    else:
        print(" Distance: ", Distance,"km")
else:
    print("Choose the correct option")         