

import random
import math
import redis

# Connecting to the redis server
redis = redis.Redis(
    host='localhost',
    port='6379')
# Storing digits from 0 to 9 in a list
digits = [i for i in range(0, 10)]

# Initializing an empty string to store the OTP
random_str = ""

# Generating a 4-digit OTP
for i in range(4):
    # Generating a random index for the list of digits
    index = math.floor(random.random() * 10) 
    random_str += str(digits[index])  

# Asking the user if they are waiting for an OTP
OrderDeliver = input("Your order is deliverd  yes/no: ").lower()

# If the user is waiting for an OTP
if OrderDeliver == "yes":
    print("OTP is Generated ")
    # Storing the OTP in the redis server for both the driver and the customer
    redis.set("OTP_Driver", random_str)
    redis.expire("OTP_Driver", 300)

    redis.set("OTP_Customer", random_str)
    redis.expire("OTP_Customer", 300)
    print("OTP: ", random_str)

# If the user is not waiting for an OTP
elif OrderDeliver == "no":
    print("Please wait for the order to be delivered")

# If the user input is invalid
else:
    print("Please enter only yes or no")


