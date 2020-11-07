import os
def docker_image():
    while True:
        os.system("clear")
        print("Welcome to the World of Docker Images\n\nPress the respective key to proceed\n\nPress 1 : To search any image on Docker Hub\nPress 2 : To see the available images on the system\nPress 3 : To download a docker image\nPress 4 : To delete a docker image\nPress 5 : To return to previous menu\nPress 6 : To exit\n")
        image_key=input("Enter your choice : ")
        if image_key=="1":
            image_name=input("Please provide the image name you want to search : ")
            os.system("docker search {}".format(image_name))
        elif image_key=="2":
            os.system("docker image ls")
        elif image_key=="3":
            download_image=input("Please provide the image name along with tag/version : ")
            os.system("docker pull {}".format(download_image))
        elif image_key=="4":
            delete_image=input("Please provide the image name along with tag you want to delete : ")
            os.system("docker rmi -f {}".format(delete_image))
        elif image_key=="5":
            return 0
        elif image_key=="6":
            exit()
        else:
            print("\nWrong Input !!!")
        input("\nEnter to continue...")

def docker_container():
    while True:
        os.system("clear")
        print("Welcome to the World of Docker Containers\n\nPress the respective key to proceed\n\nPress 1 : To see all the containers\nPress 2 : To launch a container\nPress 3 : To enter in a running container\nPress 4 : To start a stopped container\nPress 5 : To stop a running container\nPress 6 : To terminate a container\nPress 7 : To return to previous menu\nPress 8 : To exit\n")
        container_key=input("Enter your choice : ")
        if container_key=="1":
            os.system("docker ps -a")
        elif container_key=="2":
            container_image=input("\nPlease provide the image name along with tag/version : ")
            container_name=input("Please assign a name to your container : ")
            os.system("docker run -dit --name {} {}".format(container_name,container_image))
        elif container_key=="3":
            container_name_enter=input("\nPlease provide the container name you want to enter : ")
            os.system("docker exec -it {} bash".format(container_name_enter))
        elif container_key=="4":
            container_name_start=input("\nPlease provide the container name you want to start : ")
            os.system("docker start {}".format(container_name_start))
        elif container_key=="5":
            container_name_stop=input("\nPlease provide the container name you want to stop : ")
            os.system("docker stop {}".format(container_name_stop))
        elif container_key=="6":
            container_name_terminate=input("\nPlease provide the container name you want to terminate : ")
            os.system("docker rm -f {}".format(container_name_terminate))
        elif container_key=="7":
            return 0
        elif container_key=="8":
            exit()
        else:
            print("\nWrong Inpur !!!")
        input("\nEnter to continue...")



def docker():
    while True:
        os.system("clear")
        print("Welcome to the page of Docker\n\nPress the respective key to proceed\n\nPress 1 : To check if docker services is running or not\nPress 2 : To start the docker services\nPress 3 : To enter the docker image world\nPress 4 : To enter the container world\nPress 5 : To return to previous menu\nPress 6 : To exit\n")
        docker_key = input("Enter your choice : ")
        if docker_key=="1":
            os.system("systemctl status docker")
        elif docker_key=="2":
            os.system("systemctl start docker")
            print("Docker Services started successfully...")
        elif docker_key=="3":
            docker_image()
        elif docker_key=="4":
            docker_container()
        elif docker_key=="5":
            return 0
        elif docker_key=="6":
            exit()
        else:
            print("\nWrong Input !!!")
        input("\nEnter to continue...")
