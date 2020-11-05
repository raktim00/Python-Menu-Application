import os
def linux():
    while True:
        os.system("clear")
        print("Welcome to the linux basic command page\n")
        print("Press the respective key to run the commands\n")
        print("Press 1 : To run the date command")
        print("Press 2 : To see the calender command")
        print("Press 3 : To see the ip address")
        print("Press 4 : To go back to main menu")
        print("Press 5 : To exit")
        linux_key = input("Enter your choice : ")
        if linux_key=="1":
            os.system("date")
        elif linux_key=="2":
            os.system("cal")
        elif linux_key=="3":
            os.system("ifconfig")
        elif linux_key=="4":
            return 0
        elif linux_key=="5":
            exit()
        else:
            print("\nWrong Input !!!")
        input("\nEnter to continue...")

while True:
    os.system("clear")
    print("This is your personal assistant menu program\n")
    print("Press the respective key for getting outputs\n")
    print("Press 1 : Linux Basic Commands")
    print("Press 2 : To exit\n")
    key = input("Enter your desired key : ")
    if key=="1":
        linux()
    elif key=="2":
        exit()
    else:
        print("\nWorng Input !!!")
    input("\nEnter to continue...")