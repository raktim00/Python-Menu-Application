import os
def local():
    while True:
        os.system("clear")
        print("Local system basic linux commands\n")
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

def remote():
    while True:
        os.system("clear")
        print("Remote system basic linux commands\n")
        ip=input("Please provide the ip of the remote system : ")
        print("\nPress the respective key to run the commands on {} system\n".format(ip))
        print("Press 1 : To run the date command")
        print("Press 2 : To see the calender command")
        print("Press 3 : To see the ip address")
        print("Press 4 : To go back to main menu")
        print("Press 5 : To exit")
        linux_key = input("Enter your choice : ")
        if linux_key=="1":
            os.system("ssh {} date".format(ip))
        elif linux_key=="2":
            os.system("ssh {} cal".format(ip))
        elif linux_key=="3":
            os.system("ssh {} ifconfig".format(ip))
        elif linux_key=="4":
            return 0
        elif linux_key=="5":
            exit()
        else:
            print("\nWrong Input !!!")
        input("\nEnter to continue...")

def linux():
    while True:
        os.system("clear")
        print("Welcome to the linux basic command page\n")
        print("Press the respective key to proceed\n")
        print("Press 1 : To run linux commands on local system")
        print("Press 2 : To run linux connands on remote system")
        print("Press 3 : To go back to main menu")
        print("Press 4 : To exit")
        linux_key = input("Enter your choice : ")
        if linux_key=="1":
            local()
        elif linux_key=="2":
            remote()
        elif linux_key=="3":
            return 0
        elif linux_key=="4":
            exit()
        else:
            print("\nWrong Input !!!")
        input("\nEnter to continue...")