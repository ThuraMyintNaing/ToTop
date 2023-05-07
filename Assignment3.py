db = {}


def main_sector():
    main_option = input("Press 1 to Register:\nPress 2 to Login\nPress 3 Exit:")
    if main_option == '1':
        registration()
    elif main_option == '2':
        login()
    elif main_option == '3':
        recording_all_data()
        exit(2)
    else:
        print("Invalid Option:\nTry again")
        main_sector()


def registration():
    user_email = input("Enter your email:")
    email_get = email_exit(user_email)

    if email_get is not None:
        print("Email already exit:\nPlease login")
        main_sector()
    else:
        user_name = input("Enter your username:")
        user_password = input("Enter your password:")
        user_phone = input("Enter your phone:")
        user_age = input("Enter your age:")

        my_id = len(db)

        to_insert = {my_id: {"email": user_email, "u_name": user_name, "password": user_password, "phone": user_phone,
                             "age": user_age}}
        db.update(to_insert)


def login():
    user_found = -1
    print("This is login sector")
    l_user_email = input("Enter your email to login:")
    l_user_password = input("Enter your password to login:")

    for i in range(len(db)):
        if db[i]["email"] == l_user_email and db[i]["password"] == l_user_password:
            user_found = i
    if user_found != -1:
        print("Login Success!")
        user_profile(user_found)
    else:
        print("Not Found ")


def user_profile(user_found):
    print("Welcome:", db[user_found]["u_name"])
    print("Your Profile:", db[user_found])
    while True:
        change_profile(user_found)





def email_exit(email):
    length = len(db)
    for i in range(length):
        if db[i]["email"] == email:
            return i


def recording_all_data():
    with open("thura.txt", 'w') as file:
        for item in range(len(db)):
            email = db[item]["email"]
            name = db[item]["u_name"]
            password = db[item]["password"]
            phone = db[item]["phone"]
            age = db[item]["age"]
            data_profile = email + ' ' + name + ' ' + password + ' ' + phone + ' ' + age
            file.writelines(data_profile)
            file.writelines("\n")


def loading_all_data():
    open("thura.txt", 'a')
    file_read = open("thura.txt", 'r')
    data_read = file_read.readlines()
    if len(data_read) == 0:
        pass
    else:
        for i in range(len(data_read)):
            split_data = data_read[i].strip().split(" ")
            data_load = {i: {"email": split_data[0], "u_name": split_data[1], "password": split_data[2],
                             "phone": split_data[3], "age": split_data[4]}}

            db.update(data_load)


def change_profile(user_found):
    option = input("Press 1==>change your profile:\nPress 2==> not change your profile:\nPress 3==>Exit program:")
    if option == '1':
        print("Please choice number to change profile:")
        choice = input("1 for email:\n2 for username:\n3 for password:\n4 for phone:\n5 for age:")
        if choice == '1':
            db[user_found]["email"] = input("Enter you want to change email:")
        elif choice == '2':
            db[user_found]["u_name"] = input("Enter you want to change u_name:")
        elif choice == '3':
            db[user_found]["password"] = input("Enter you want to change password:")
        elif choice == '4':
            db[user_found]["phone"] = int(input("Enter you want to change phone:"))
        elif choice == '5':
            db[user_found]["age"] = input("Enter you want to change age:")
        else:
            print("Your choice is not true")
        print("Your profile:", db[user_found])
    elif option == '2':
        print("Your profile:", db[user_found])
    elif option == '3':
        print("Your are exit our program")
        recording_all_data()
        exit(1)
    else:
        print("Invalid option")
        change_profile(user_found)


if __name__ == '__main__':
    loading_all_data()
    while True:
        main_sector()
