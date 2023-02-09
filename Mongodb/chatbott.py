import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["courier_db"]
deliveries = db["deliveries"]

def courier_chatbot():
    print("Welcome to the Courier Delivery Chatbot! How can I help you today?")
    while True:
        user_input = input("You: ")
        if "track" in user_input.lower():
            tracking_id = input("Please enter your tracking ID: ")
            info = db.deliveries.find({"tracking_id": tracking_id})
            #tracking_info = retrieve_tracking_info(tracking_id)
            for i in info:
                print("Tracking ID:"+ i['tracking_id'])
                print("Tracking_info:"+ i['tracking_info'])
                print("Name:"+ i['first_name'])
                print(f"Your package will be deliverd on  {i['Delivery date']}")
            if info:
                print("Tracking ID " + tracking_id )
            
            else:
                print("Tracking ID " + tracking_id + " not found.")
        elif "help" in user_input.lower():
            print("Here are some things you can ask me:")
            print("- Track your package (e.g. 'track my package')")
            print("- Get delivery status (e.g. 'where is my package')")
            print("- Exit (e.g. 'quit')")
        elif "quit" in user_input.lower():
            print("Thank you for using our chatbot! Have a great day!")
            break
        else:
            print("Sorry, I didn't understand what you meant. Try asking for help.")

#def retrieve_tracking_info(tracking_id):
    
    
  

if __name__ == '__main__':
    courier_chatbot()