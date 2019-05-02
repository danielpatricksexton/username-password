

dictionary = {
    "facebook": {"username": "daniel@facebook", "password": "1234"},
    "twitter": {"username2": "daniel@twitter.com", "password2": "5678"},
    "instagram": {"username3": "daniel@instagram.com", "password3": "4321"},
}
print("""1. Facebook
2. twitter
3. Instagram""")
user_input = input("Which account do you want to see: ")

while user_input.lower() != "n":
    if user_input == "1":
        print("username: ", dictionary["facebook"]["username"])
        print("password: ", dictionary["facebook"]["password"])
    elif user_input == "2":
        print("username: ", dictionary["twitter"]["username2"])
        print("password: ", dictionary["twitter"]["password2"])
    elif user_input == "3":
        print("username: ", dictionary["instagram"]["username3"])
        print("password: ", dictionary["instagram"]["password3"])
    else:
        print("please try again")
    ask_option = input("Do you want to try again? Y/N:")
    if ask_option.lower() == "Y":
        user_input = input("Which account do you want to see: ")
    else:
        break
