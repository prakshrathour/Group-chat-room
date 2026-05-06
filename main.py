import json
from datetime import datetime
def load_data():
    with open("data.json", "r") as file:
        return json.load(file)
def save_data(user):
    with open("data.json", "w") as file:
        json.dump(user, file, indent=4)

def log_in():
    user_name = input("Enter your Name : ")
    print(f"Logged in as {user_name}")
    
    return user_name  

def send_message(user_name, room_name):
    msg=input("Enter your message : ")
    if not msg:
        print("It can not be empty .")
        return
    user[room_name].append({
        "name": user_name,
        "message": msg,
        "time": datetime.now().strftime("%I:%M %p | %d-%m-%Y")
    })
    save_data(user)

def view_message(room_name):
    if not user[room_name]:
        print("No messages yet")
        return
    for i in range(len(user[room_name])):
        print(f"{user[room_name][i]['time']}  {user[room_name][i]['name']} : {user[room_name][i]['message']}")

def select_room():
    print("Choose one Option : ")
    print("1. Join Existing room .")
    print("2. Create room .")
    room_choice=int(input("Enter your choice : "))
    while room_choice not in [1,2]:
        print("Invalid choice.")
        room_choice=int(input("Enter your choice : "))
    if room_choice==1:
        print(f"Available rooms are :")
        for room_name in user:
            print(room_name)
            
        room_name=input("Enter the room name : ").strip().lower()
        while room_name not in user:
            print("Room not Found...")
            room_name=input("Enter the room name : ")
        return room_name
    elif room_choice == 2:
        newroom_name = input("Enter the name for the new room : ").strip().lower()

        if newroom_name in user:
            print("Room already exists.")
            return newroom_name

        user[newroom_name] = []   
        save_data(user)           

        print(f"Room '{newroom_name}' created!")
        return newroom_name

while True:
    user=load_data()
    user_name=log_in()
    room_name=select_room()
    print(f'Welcome to the Room {room_name}')
    while True:
        print("1. Send message .")
        print("2. View message .")
        print("3. Change room .")
        print("4. Change user .")
        print("5. Log Out .")
        choice=int(input("Enter your choice : "))
        while choice not in [1,2,3,4,5]:
            print("Invalid choice.")
            choice=int(input("Enter your choice : "))
        if choice ==1:
            send_message(user_name, room_name)
        elif choice ==2:
            load_data()
            view_message(room_name)
        elif choice ==3:
            room_name = select_room()
        elif choice ==4:
            user_name=log_in()
        elif choice ==5:
            print("Logging Out...")
            break
    print("You have been logged out , Choose one option : ")
    print("1. Log in again .")
    print("2. Exit  .")
    final_choice=int(input("Enter your choice : "))
    while final_choice not in [1,2]:
        print("Invalid choice..")
        final_choice=int(input("Enter your choice : "))

    if final_choice ==2:
        break
        