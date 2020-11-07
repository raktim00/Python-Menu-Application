import os
def hadoopslave_local():
	while True:
		os.system("clear")
		print("------------------------Hadoop datanode local configuration---------------------\n")
		print("Press the respective key to run the commands:\n")
		print("""
		\n
		Press 1: To configure the hadoop datanode
		Press 2: To start the datanode service
		Press 3: To check the datanode service
		Press 4: To stop the datanode service
		Press 5: To go back to previous menu
		Press 6: To exit
		""")
		choice = input("enter choice:")
		if int(choice) == 1:
				mip = input("enter master ip:")
				print("Hadoop slave node configured!!")
				os.system("mkdir /etc/hadoop/dn")
				os.system("echo  \"<configuration>\n<property>\n<name>dfs.name.dir</name>\n<value>/nn</value>\n</property>\n</configuration> \" > /etc/hadoop/hdfs-site.xml")
				os.system("echo -e \"<configuration>\n<property>\n<name>fs.default.name</name>\n<value>{}:9001</value>\n</property>\n</configuration> \" > /etc/hadoop/core-site.xml".format(mip))
		elif int(choice) == 2:
				os.system("hadoop-daemon.sh start datanode ")
		elif int(choice) == 3:
				os.system("jps")
		elif int(choice) == 4:
				os.system("hadoop-daemon.sh stop datanode ")
		elif int(choice) == 5:
				return 0
		elif int(choice) == 6:
				exit()
				
		else:
				print("not supported login....")
		input("\nEnter to continue...")

def hadoopslave_remote():
	while True:
		os.system("clear")
		print("------------------------Hadoop datanode remote configuration--------------------\n")
		print("Press the respective key to run the commands:\n")
		print("""
		\n
		Press 1: To configure the hadoop datanode
		Press 2: To start the datanode service
		Press 3: To check the datanode service
		Press 4: To stop the datanode service
		Press 5: To go to previous menu
		Press 6: To exit
		""")
		ip = input("enter remote ip:")
		print(ip)
		choice = input("enter choice:")
		if int(choice) == 1:
				mip = input("enter master ip:")
				os.system("ssh {} mkdir /etc/hadoop/dn".format(ip))
				os.system("echo -e \"<configuration>\n<property>\n<name>dfs.name.dir</name>\n<value>/nn</value>\n</property>\n</configuration> \" > /etc/hadoop/hdfs-site.xml")
				os.system("scp /etc/hadoop/hdfs-site.xml {}:/etc/hadoop".format(ip))
				os.system("echo -e \"<configuration>\n<property>\n<name>fs.default.name</name>\n<value>{}:9001</value>\n</property>\n</configuration> \" > /etc/hadoop/core-site.xml".format(mip))
				os.system("scp /etc/hadoop/core-site.xml {}:/etc/hadoop".format(ip))
		elif int(choice) == 2:
				os.system("ssh {} hadoop-daemon.sh start datanode ".format(ip))
		elif int(choice) == 3:
				os.system("ssh {} jps".format(ip))

		elif int(choice) == 4:
				os.system("ssh {} hadoop-daemon.sh stop datanode ".format(ip))
		elif int(choice) == 5:
				return 0
		elif int(choice) == 6:
				exit()
		else:
				print("not supported login....")
		input("\nEnter to continue...")

def hadoop_slave():
	while True:
		os.system("clear")
		print("---------------------------Hadoop datanode configuration------------------------\n")
		print("Press the respective key to run the commands:\n")
		print("""
		\n
		Press 1: To configure hadoop datanode on local syastem
		Press 2: To configure hadoop datanode on remote system
		Press 3: To go back to main menu
		Press 4: To exit
		""")
		slave_choice=input("Enter your choice: ")
		if int(slave_choice) == 1:
				hadoopslave_local()
		elif int(slave_choice) == 2:
				hadoopslave_remote()
		elif int(slave_choice) == 3:
				return 0
		elif int(slave_choice) == 4:
				exit()
		else:
			print("\n Wrong input")
		input("\nEnter to continue...")