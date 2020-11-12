import os
import getpass
def hadoop_master():
	while True:
		os.system("clear")
		os.system("tput setaf 3")
		print("CHOOSE FROM THE BELOW KEYS :\n")
		print("""
		Press 1 : CONFIGURE HADOOP MASTER NODE
		Press 2 : START MASTER NODE SERVICE
		Press 3 : CHECK STATUS OF MASTER NODE
		Press 4 : STOP MASTER NODE SERVICE
		Press 5 : PREVIOUS MENU
		Press 6 : EXIT\n 
		""")
		os.system("tput setaf 7")
		choice = int(input("ENTER CHOICE : "))

		if choice==1:
			r_ip=input("ENTER IP OF REMOTE SYSTEM WHICH YOU WANT TO USE AS MASTER: ")
			r_pwd=getpass.getpass("YOU WOULD HAVE TO ENTER THE PASSWORD TWICE....\n root@{}'s password : ".format(r_ip))
			os.system("scp /root/hadoop-1.2.1-1.x86_64.rpm {}:/root/".format(r_ip))
			os.system("sshpass -p {} scp /root/jdk-8u171-linux-x64.rpm {}:/root/".format(r_pwd,r_ip))
			os.system("sshpass -p {} ssh {} rpm -ivh jdk-8u171-linux-x64.rpm".format(r_pwd,r_ip))
			os.system("sshpass -p {} ssh {} rpm -ivh hadoop-1.2.1-1.x86_64.rpm --force ".format(r_pwd,r_ip))
			os.system("tput setaf 3")	
			mdir=input("ENTER ANY NAME FOR DIRECTORY : ")
			os.system("tput setaf 7")
			dircheck=os.system("sshpass -p {} ssh {} mkdir /etc/hadoop/{}".format(r_pwd,r_ip,mdir))
			if dircheck != 0:
				os.system("tput setaf 1")
				print("THERE WAS SOME ISSUE WITH THIS DIRECTORY NAME...")
				os.system("tput setaf 7")
				mdir=input("ENTER OTHER DIRECTORY NAME : ")
				os.system("sshpass -p {} ssh {} mkdir /etc/hadoop/{}".format(r_pwd,r_ip,mdir))
			elif dircheck==0:
				os.system("tput setaf 2")
				print("DIRECTORY HAS BEEN SUCCESSFLLY CREATED...")
				os.system("tput setaf 7")
			
			os.system("echo -e \"<?xml version='1.0'?>\n<?xml-stylesheet type='text/xsl' href='configuration.xsl'?>\n<!-- Put site-specific property overrides in this file. -->\n<configuration>\n<property>\n<name>dfs.name.dir</name>\n<value>/{}</value>\n</property>\n</configuration> \" > /etc/hadoop/hdfs-site.xml".format(mdir))
			os.system("scp /etc/hadoop/hdfs-site.xml {}:/etc/hadoop/hdfs-site.xml".format(r_ip))


			os.system("echo -e \"<?xml version='1.0'?>\n<?xml-stylesheet type='text/xsl' href='configuration.xsl'?>\n<!-- Put site-specific property overrides in this file. -->\n<configuration>\n<property>\n<name>fs.default.name</name>\n<value>hdfs://0.0.0.0:9001</value>\n</property>\n</configuration>\" > /etc/hadoop/core-site.xml")
			os.system("scp /etc/hadoop/core-site.xml {}:/etc/hadoop/core-site.xml".format(r_ip))


			os.system("tput setaf 2")			
			print("HADOOP MASTER NODE HAS BEEN SUCCESSFULLY CONFIGURED...")
			os.system("tput setaf 4")
			input("ENTER TO CONTINUE....")
			os.system("tput setaf 7")
		elif choice==2:
			os.system("sshpass -p {} ssh {} hadoop namenode -format".format(r_pwd,r_ip))
			os.system("sshpass -p {} ssh {} systemctl stop firewalld".format(r_pwd,r_ip))
			os.system("sshpass -p {} ssh {} hadoop-daemon.sh start namenode".format(r_pwd,r_ip))
			os.system("tput setaf 2")
			print("HADOOP MASTER NODE SERVICE HAS BEEN SUCESSFULLY STARTED")
			os.system("tput setaf 4")
			input("ENTER TO CONTINUE....")
			os.system("tput setaf 7")
		elif choice==3:
			os.system("sshpass -p {} ssh {} jps".format(r_pwd,r_ip))
			input("ENTER TO CONTINUE....")
		elif choice==4:
			os.system("sshpass -p {} ssh {} hadoop-daemon.sh stop namenode".format(r_pwd,r_ip))
			os.system("sshpass -p {} ssh {} jps".format(r_pwd,r_ip))
			os.system("tput setaf 2")
			print("THE HADOOP MASTER SERVICE HAS BEEN SUCCESSFULLY STOPPED...")
			os.system("tput setaf 4")
			input("ENTER TO CONTINUE....")
			os.system("tput setaf 7")
		elif choice==5:
			return 0
		elif choice==6:
			exit()
		os.system("tput setaf 7")
def hadoop_slave():
	while True:
		print("------------------------Hadoop datanode---------------------\n")
		print("Press the respective key to run the commands:\n")
		print("""
		\n
		Press 1 : CONFIGURE HADOOP DATA NODE
		Press 2 : START DATA NODE SERVICE
		Press 3 : CHECK STATUS OF DATA NODE
		Press 4 : STOP DATA NODE SERVICE
		Press 5 : EXIT
		""")
		choice = input("enter choice:")
		if choice == "1":
				mip = input("enter master ip:")
				print("Hadoop slave node configuration!!")
				#os.system("mkdir /etc/hadoop/dn")
				os.system("df -h")
				dirname=input("YOU NEED TO GIVE THE SAME DIRECTORY NAME WHICH YOU GAVE IN LVM (you can refer above table):")
				os.system("echo  \"<configuration>\n<property>\n<name>dfs.name.dir</name>\n<value>/{}</value>\n</property>\n</configuration> \" > /etc/hadoop/hdfs-site.xml".format(dirname))
				os.system("echo -e \"<configuration>\n<property>\n<name>fs.default.name</name>\n<value>{}:9001</value>\n</property>\n</configuration> \" > /etc/hadoop/core-site.xml".format(mip))
		elif choice == "2":
				os.system("hadoop-daemon.sh start datanode ")
		elif choice == "3":
				os.system("systemctl stop firewalld")
				os.system("jps")
		elif choice == "4":
				os.system("hadoop-daemon.sh stop datanode ")
		elif choice == "5":
				return 0
		elif choice == "6":
				exit()
				
		else:
				print("not supported login....")
		input("\nEnter to continue...")

def lvm():
		os.system("tput setaf 3")
		os.system("tput setaf 2")
		print("\tCREATING LVM PARTITIONS\t\n")
		os.system("tput setaf 7")
		pvlist=[]
		os.system("tput setaf 3")
		disknum=int(input("ENTER NUMBER OF NEW DISKS YOU ATTACHED"))
		os.system("tput setaf 7")
		for i in range(disknum):
			os.system("tput setaf 3")
			diskname=input("ENTER THE NAME OF THE NEW DISK ATTACHED eg. /dev/sda")
			os.system("tput setaf 7")
			if diskname in pvlist:
				os.system("wipefs -a {}".format(diskname))		
			pvlist.append(diskname)
			pvlist.reverse()
			os.system("pvcreate {}".format(diskname))
			os.system("tput setaf 3")
			print("CONVERTING YOUR HARD DRIVE => PHYSICAL VOLUME.....")
		print("THE AVAILABLE PHYSICAL VOLUMES ARE : ")
		os.system("tput setaf 7")
		os.system("pvdisplay")
		os.system("tput setaf 3")
		print("NOW WE HAVE TO CREATE VOLUME GROUP.....")
		os.system("tput setaf 7")
		vg_list1=[]
		vg_list2=[]
		os.system("tput setaf 3")
		vg_name=input("GIVE ANY NAME FOR VOLUME GROUP :")
		os.system("tput setaf 7")
		vg_list1.append(vg_name)
		if vg_name in vg_list2:
			os.system("tput setaf 3")
			print("VOLUME GROUP ALREADY EXISTS.. KINDLY USE ANOTHER NAME")
			os.system("tput setaf 7")
			ch=input("DO YOU WANT TO REMOVE THE PREVIOUS CREATED VG (Y/N) : ")
			if ch == "y" or ch == "Y":
				os.system("vgremove {}".format(vg_name))
			else : 
				pass
			vg_name = input("ENTER NEW VG NAME : ")
			vg_list2.append(vg_name)
		os.system("tput setaf 3")
		print("CREATING VOLUME GROUPS...")
		os.system("tput setaf 7")
		pvnum=pvlist.pop()
		os.system("vgcreate {} {}".format(vg_name,pvnum))
		#EXTENDING THE VG TO MAKE IT DYNAMIC
		for i in pvlist:
			os.system("vgextend {} {}".format(vg_name,i))
		os.system("tput setaf 3")
		print("VOLUME GROUPS CREATED ARE AS FOLLOWS ")
		os.system("tput setaf 7")
		os.system("vgdisplay {}".format(vg_name))
		lvnum=int(input("ENTER NUMBER OF LOGICAL VOLUMES YOU WANT TO CREATE : "))
		lvlist1=[]
		lvlist2=[]
		lvsize=[]
		for i in range(lvnum):
			os.system("tput setaf 3")
			lvname=input("ENTER NAME OF THE LOGICAL VOLUME YOU WANT TO GIVE :")
			lvlist1.append(lvname)
			size=input("ENTER THE SIZE OF THE LOGICAL VOLUME :")
			if lvname in lvlist2:
				os.system("lvremove /dev/{}/{}".format(vg_name,lvname))		
				lvname=input("ENTER ANOTHER NAME OF LV :")	
					
			os.system("lvcreate --size {} --name {} {}".format(size,lvname,vg_name)) 
			lvlist2.append(lvname)	
			print("THE LOGICAL VOLUMES CREATED ARE : ")
			os.system("lvdisplay {}/{}".format(vg_name,lvname))
			print("FORMATTING THE CREATED PARTITIONS .... \n CREATING THE INODE TABLE",os.system("mkfs.ext4 /dev/{}/{}".format(vg_name,lvname)))	
			dirname=input("ENTER A DIRECTORY NAME TO MOUNT TO THIS DEVICE :")
			os.system("mkdir /{}".format(dirname))
			print("MOUNTING THE CREATED DIRECTORY TO THE DEVICE :",os.system("mount /dev/{}/{} /{}".format(vg_name,lvname,dirname)))
			os.system("tput setaf 7")


def extending_storage_of_datanode():
	print("increasing storage of datanode using lvm concept")
	print("USING THE ABOVE TABLE SELECT LV NAME OF YOUR DIRECTORY ...")
	os.system("df -h")
	size = input("ENTER SIZE YOU WANT TO ADD MORE {in K/M/G} : ")
	print("USE VOLUME GROUP AND LOGICAL VOLUME ACCORDINGLY..") 
	os.system("vgdisplay")
	vg_name=input("ENTER VG NAME : ")
	os.system("lvdisplay")
	lvname=input("ENTER LV NAME : ")
	os.system("lvextend --size +{} /dev/{}/{}".format(size,vg_name,lvname))
	s=os.system("resize2fs /dev/{}/{}".format(vg_name,lvname))
	if s == 0:
		print("SIZE OF THE STORAGE IN DATANODE HAS BEEN INCREASED SUCCESSFULLY")

	else:
		print("THERE WAS SOME PROBLEM ...")

def reducing_storage_of_datanode():
	print("decreasing storage of datanode using lvm concept")
	print("USING THE ABOVE TABLE SELECT LV NAME OF YOUR DIRECTORY ...")
	os.system("df -h")
	size = input("ENTER SIZE YOU WANT FINALLY IN YOUR DATANODE {in K/M/G} : ")
	print("USE VOLUME GROUP AND LOGICAL VOLUME ACCORDINGLY..") 
	os.system("vgdisplay")
	vg_name=input("ENTER VG NAME : ")
	os.system("lvdisplay")
	lvname=input("ENTER LV NAME : ")
	os.system("lvreduce --resize --size {} /dev/{}/{}".format(size,vg_name,lvname))

	if s == 0:
		print("SIZE OF THE STORAGE IN DATANODE HAS BEEN INCREASED SUCCESSFULLY")

	else:
		print("THERE WAS SOME PROBLEM ...")
	os.system("mount /dev/{}/{} {}".format(vg_name,lvname,dirname))
	os.system("df -h")

def web_server_on_docker():
	cont_name=input("ENTER CONTAINER NAME YOU WANT TO GIVE : ")
	os.system("docker run -it --name {} centos:latest".format(cont_name))
	os.system("yum install net-tools")
	os.system("yum install httpd")
	
	os.system("cd /var/www/html")
	os.system("/usr/sbin/httpd")
	os.system("netstat -tnlp ")
	os.system("tput setaf 2")
	print("HTTPD SERVICE HAS BEEN STARTED...")
	print("WEB SERVER HAS BEEN CONFIGURED...")
	os.system("tput setaf 7")
	os.system("")
	
def docker_python():
	os.system("yum install python36 -y")
	os.system("python3")
	os.system("echo 'print(\"Hello! this is python....running\")' > a.py")
	os.system("python3 a.py")
	os.system("sleep 5")


def main():
	dirname=""
	while True:
		os.system("clear")
		print("\t******WELCOME TO THE AUTOMATED TASK 7.1******\t\t\n")
		print("\t******PRESS 1 : FOR LVM PARTITIONING******\n\t******PRESS 2 : FOR HADOOP MASTERNODE******\n\t******PRESS 3 : FOR HADOOP DATANODE******\n\t******PRESS 4 : FOR INCREASING THE STORAGE OF DATANODE******\n\t******PRESS 5 : FOR DECREASING THE STORAGE OF DATANODE******\n\t******PRESS 6 : WEB SERVER CONFIGURATION ON DOCKER CONTAINER******\n\t******PRESS 7 : FOR PYTHON ON DOCKER CONTAINER******\n\t******PRESS 8 : TO QUIT******\n")
		ch1=input("ENTER YOUR CHOICE HERE : ")
		if ch1 == "1":
			lvm()
		elif ch1 == "2":
			hadoop_master()
		elif ch1 == "3":
			hadoop_slave()
		elif ch1 == "4":
			extending_storage_of_datanode()
		elif ch1 == "5":
			reducing_storage_of_datanode()
		elif ch1 == "6":
			web_server_on_docker()
		elif ch1 == "7":
			exit()
		else:
			print("INVALID CHOICE...TRY AGAIN")

main()
		
