import pymongo
from pymongo import MongoClient
import ssl
import smtplib
from email.message import EmailMessage

# Create Connection
client = MongoClient('localhost', port= 27017)
database= client["Coupons"]
collection= database['Customers']

#Create Pipeline
pipeline= collection.aggregate(
    [
        {
            "$match": {"TotalConfirmedOrders": {"$gt": "5"}}
        },
        {
            "$project": {"CustomerId":1, "FullName":1, "Email":1, "TotalConfirmedOrders":1}
        },
        {
            "$limit": 1001
        }
    ]
)

for items in pipeline:
    emails= items['Email']
    Full_name= items['FullName']
    print(items)


# Code for Email.
def sendInvite():
    email_sender= 'harrypatel270@gmail.com'
    email_receiver= 'harshdeutschland@gmail.com'
    password= 'qmdqmkqxpmulelyq'
    subject=" Test Email!"
    body= f"   Hey {Full_name}! Thank You for being a loyal customer with us." \
          " As a gift of appreciation we would like to give you a 25% COUPON." \
          " You can use this coupon on your next Order!\n" \
          "       " \
          "" \
          f"Hey {Full_name}! Vielen Dank, dass Sie ein treuer Kunde bei uns sind." \
          "Als Dankeschön möchten wir Ihnen einen 25 % GUTSCHEIN schenken." \
          "Diesen Gutschein können Sie bei Ihrer nächsten Bestellung verwenden!"

    msg= EmailMessage()
    msg['from']= email_sender
    msg['to']= email_receiver
    msg['Subject']= subject
    msg.set_content(body)
    context = ssl.create_default_context() # Setting our SSL server
    smtp= smtplib.SMTP_SSL('smtp.gmail.com',port=465 , context=context) # providing port and connection information
    smtp.login(email_sender,password)
    smtp.sendmail(email_sender,email_receiver,msg.as_string())

sendInvite()


"""db.Coupons.aggregate
{[
 // Stage One
{$match: {TotalConfirmedOrders: {
$gt: "5"
}
}
},
// Stage Two
{$limit: "10"},

// Stage Three
{$project: {
    CustomerId: 1,
    FullName: 1,
    email:1,
    TotalConfirmedOrders: 1
}
}

]
}"""