import socket
import sys
import threading
import pickle

class Servidor(object):
	"""Servidos basico para chat, hecho en python3 """
	def __init__(self, host='10.3.32.13',port=8000):
		self.clients = []

		self.sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
		self.sock.bind((host,port))
		self.sock.listen(5)
		self.sock.setblocking(False)

		# hilos para mandar msj y aceptar las conexiones		
		acept = threading.Thread(target = self.acept_client)
		connect = threading.Thread(target = self.recv_msg)

		acept.daemon = True
		acept.start()

		connect.daemon = True
		connect.start()

		# bucle con la condicion de fin para el servidor		
		while True:
			message = input('> ')
			if message == 'salir':														
				self.sock.close()
				sys.exit()	


	def acept_client(self):
		print("Acepta clientes")
		while True:			
			try:
				client_socket_server, client_address = self.sock.accept()
				client_socket_server.setblocking(False)
				self.clients.append(client_socket_server)
			except:
				pass
	
	def send_msg_clients(self,msg,client):
		for receiver in self.clients:
			try:
				if receiver != client:
					receiver.send(msg)
			except:
				self.clients.remove(receiver)
            
	def recv_msg(self):
		print("Recibe mensajes")
		while True:
			if len(self.clients) > 0:
				for client_socket in self.clients:
					try:
						msg = client_socket.recv(1024)
						if msg:
							self.send_msg_clients(msg,client_socket)
							mensaje=str(msg)
							mensaje=mensaje.replace("'","")
							mensaje=mensaje[1:]
							print (mensaje)
					except:
						pass

serv = Servidor()