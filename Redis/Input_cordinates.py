import redis

redis = redis.Redis(
    host='localhost',
    port='6379')


def enterlocation():
    Longitude = float(input("Longitude: "))
    Latitude = float(input("Latitude: "))
    Name = input("Enter  name: ")
    redis.geoadd(Keyname, (Longitude, Latitude, Name))


List = ["Delivery", "Driver","parcel_shop","PickUp"]
print("Please Choose a key as 1, 2, 3, 4 from : \n 1. Delivery \n 2. Driver \n 3. parcel_shop \n 4. PickUp \n 5. Enter new Key")
i = input("Enter - ")
i = int(i)

if i <= 4:
    i = i-1
    Keyname = List[i]
    print(Keyname)
    enterlocation()

elif i == 5:
    Keyname = input("Key: ")
    print(Keyname)
    enterlocation()
else:
    print("Choose correct option")
