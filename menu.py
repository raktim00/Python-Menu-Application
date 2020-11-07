import os
from linux import linux
from docker import docker

while True:
    os.system("clear")
    print("This is your personal assistant menu program\n\nPress the respective key for getting outputs\n\nPress 1 : Linux Basic Commands\nPress 2 : Enter Docker World\nPress 3 : To exit\n")
    key = input("Enter your desired key : ")
    if key=="1":
        linux()
    elif key=="2":
        docker()
    elif key=="3":
        exit()
    else:
        print("\nWorng Input !!!")
    input("\nEnter to continue...")
