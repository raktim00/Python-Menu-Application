from hadoop_slave import hadoop_slave
import os

def hadoop():
	while True:
		os.system("clear")
		print("----------------------------Welcome to Hadoop World----------------------------\n")
		print("Press the respective key to run the commands:\n")
		print("""
		\n
		Press 1: To configure hadoop master node
		Press 2: To configure hadoop slave node
		Press 3: To configure hadoop client
		Press 4: To check hadoop cluster
		Press 5: To go back to main menu
		Press 6: To exit
		""")
		ch=input("Enter your choice: ")
		if int(ch) == 2:
				hadoop_slave()
		elif int(ch) == 4:
				os.system("hadoop dfsadmin -report")
		elif int(ch) == 5:
				return 0
		elif int(ch) == 6:
				exit()
		else:
			print("\n Wrong input")
		input("\nEnter to continue...")
	
