import os
import getpass
#-----------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------
def master_local():
	while True:
		os.system("tput setaf 3")
		print("Press the respective key to run the commands:\n")
		print("""
		\n
		Press 1: To configure the hadoop Master Node
		Press 2: To start the Master node service
		Press 3: To check the Master node service
		Press 4: To stop the Master node service
		Press 5: To go to Menu again
		Press 6: To Exit 
		\n""")
		os.system("tput setaf 7")
		choice = int(input("Enter Choice:"))
		dirlist1=dirlist2=[]
		if choice==1:		
			os.system("tput setaf 3")	
			dirname=input("ENTER ANY NAME FOR DIRECTORY : ")
			os.system("tput setaf 7")
			dircheck=os.system("mkdir /etc/hadoop/{}".format(dirname))
			if dircheck != 0:
				os.system("tput setaf 1")
				print("THERE WAS SOME ISSUE WITH THIS DIRECTORY NAME...")
				os.system("tput setaf 3")
				dirname=input("ENTER OTHER DIRECTORY NAME : ")
				os.system("tput setaf 7")
				os.system("mkdir /etc/hadoop/{}".format(dirname))
			elif dircheck==0:
				os.system("tput setaf 2")
				print("DIRECTORY HAS BEEN SUCCESSFLLY CREATED...")
				os.system("tput setaf 7")
			os.system("echo -e \"<?xml version='1.0'?>\n<?xml-stylesheet type='text/xsl' href='configuration.xsl'?>\n<!-- Put site-specific property overrides in this file. -->\n<configuration>\n<property>\n<name>dfs.name.dir</name>\n<value>/{}</value>\n</property>\n</configuration> \" > /etc/hadoop/hdfs-site.xml".format(dirname))


			os.system("echo -e \"<?xml version='1.0'?>\n<?xml-stylesheet type='text/xsl' href='configuration.xsl'?>\n<!-- Put site-specific property overrides in this file. -->\n<configuration>\n<property>\n<name>fs.default.name</name>\n<value>hdfs://0.0.0.0:9001</value>\n</property>\n</configuration>\" > /etc/hadoop/core-site.xml")
			os.system("tput setaf 2")			
			print("HADOOP MASTER NODE HAS BEEN SUCCESSFULLY CONFIGURED...")
			os.system("tput setaf 4")
			input("ENTER TO CONTINUE....")
			os.system("tput setaf 7")
		elif choice==2:
			os.system("hadoop namenode -format")
			os.system("systemctl stop firewalld")
			os.system("hadoop-daemon.sh start namenode")
			os.system("tput setaf 2")
			print("HADOOP MASTER NODE SERVICE HAS BEEN SUCCESSFULLY STARTED")
			os.system("tput setaf 4")
			input("ENTER TO CONTINUE....")
			os.system("tput setaf 7")
		elif choice==3:
			os.system("jps")
			os.system("tput setaf 4")
			input("ENTER TO CONTINUE....")
			os.system("tput setaf 7")
		elif choice==4:
			os.system("hadoop-daemon.sh stop namenode")
			os.system("jps")
			os.system("tput setaf 2")
			print("THE HADOOP MASTER SERVICE HAS BEEN SUCCESSFULLY STOPPED...")
			os.system("tput setaf 4")			
			input("ENTER TO CONTINUE....")
			os.system("tput setaf 7")
		elif choice==5:
			return 0
		elif choice==6:
			exit()
#-----------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------

def master_remote():
	while True:
		os.system("clear")
		os.system("tput setaf 3")
		print("Hadoop Master Node Configuration\nPress the respective key to run the commands:\n")
		print("""
		Press 1: To configure the hadoop Master Node
		Press 2: To start the Master node service
		Press 3: To check the Master node service
		Press 4: To stop the Master node service
		Press 5: To go to Menu again
		Press 6: To Exit\n 
		""")
		os.system("tput setaf 7")
		choice = int(input("Enter Choice:"))

		if choice==1:
			r_ip=input("ENTER IP OF REMOTE SYSTEM WHICH YOU WANT TO USE AS MASTER: ")
			r_pwd=getpass.getpass("YOU WOULD HAVE TO ENTER THE PASSWORD TWICE....\n root@{}'s password : ".format(r_ip))
			os.system("scp /root/ hadoop-1.2.1-1.x86_64.rpm {}:/root/".format(r_ip))
			os.system("sshpass -p {} scp /root/ jdk-8u171-linux-x64.rpm {}:/root/".format(r_pwd,r_ip))
			os.system("sshpass -p {} ssh {} rpm -ivh jdk-8u171-linux-x64.rpm".format(r_pwd,r_ip))
			os.system("sshpass -p {} ssh {} rpm -ivh hadoop-1.2.1-1.x86_64.rpm --force ".format(r_pwd,r_ip))
			os.system("tput setaf 3")	
			dirname=input("ENTER ANY NAME FOR DIRECTORY : ")
			os.system("tput setaf 7")
			dircheck=os.system("sshpass -p {} ssh {} mkdir /etc/hadoop/{}".format(r_pwd,r_ip,dirname))
			if dircheck != 0:
				os.system("tput setaf 1")
				print("THERE WAS SOME ISSUE WITH THIS DIRECTORY NAME...")
				os.system("tput setaf 7")
				dirname=input("ENTER OTHER DIRECTORY NAME : ")
				os.system("sshpass -p {} ssh {} mkdir /etc/hadoop/{}".format(r_pwd,r_ip,dirname))
			elif dircheck==0:
				os.system("tput setaf 2")
				print("DIRECTORY HAS BEEN SUCCESSFLLY CREATED...")
				os.system("tput setaf 7")
			
			os.system("echo -e \"<?xml version='1.0'?>\n<?xml-stylesheet type='text/xsl' href='configuration.xsl'?>\n<!-- Put site-specific property overrides in this file. -->\n<configuration>\n<property>\n<name>dfs.name.dir</name>\n<value>/{}</value>\n</property>\n</configuration> \" > /etc/hadoop/hdfs-site.xml".format(dirname))
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
			#-----------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------

def hadoop_master():
	while True:
		os.system("clear")
		os.system("tput setaf 3")
		print("Hadoop Master Node Configuration\nHOW WOULD YOU LIKE TO CONFIGURE HADOOP MASTER\n")
		print("""PRESS 1 : FOR LOCAL SYSTEM \nPRESS 2 : FOR REMOTE SYSTEM\nPRESS 3: TO RETURN TO PREVIOUS MENU\nPRESS 4: TO EXIT\n
		""")
		os.system("tput setaf 7")
		choice=int(input("ENTER YOUR CHOICE : "))
		if choice == 1:
			master_local()
		elif choice == 2:
			master_remote()
		elif choice == 3: 
			return 0
		elif choice ==4:
			exit()
		else:
			os.system("tput setaf 1")
			print("INVALID OPTION ....")
			os.system("tput setaf 7")			
hadoop_master()

#-----------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------







