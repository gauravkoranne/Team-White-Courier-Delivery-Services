import redis


redis = redis.Redis(
    host='localhost', 
    port='6379') 

# Define a list of key options
List = ["PickUp", "Driver", "Parcel_shop","Delivery"]

# Prompt the user to select a key option
print("Please Choose a key option as 1, 2, 3, 4 from : \n 1. PickUp \n 2. Driver \n 3. Warehouse \n 4. Delivery")
i = input("Enter - ")

i = int(i)

# Check if the user entered a valid key option
if i <= 4:
# Convert the key option to an index for the list
    i = i-1
    Keyname = List[i]
else:
    
    print("Enter correct key")


Name = input("Enter name: ")

Location = redis.geopos(Keyname, Name)

if Location == [None]:
    print("Enter correct details since you have entered wrong details")
else:
    print(" Coordinates: ", Location)
