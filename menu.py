import os
from linux import linux

while True:
    os.system("clear")
    print("This is your personal assistant menu program\n")
    print("Press the respective key for getting outputs\n")
    print("Press 1 : Linux Basic Commands")
    print("Press 2 : Enter Docker World")
    print("Press 3 : To exit\n")
    key = input("Enter your desired key : ")
    if key=="1":
        linux()
    elif key=="3":
        break
    else:
        print("\nWorng Input !!!")
    input("\nEnter to continue...")