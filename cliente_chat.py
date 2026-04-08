import socket
import threading

def recibir_mensajes(servidor_socket):
    while True:
        mensaje = servidor_socket.recv(1024).decode("utf-8")        
        print(mensaje)

# Crear el socket para el cliente
cliente_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
cliente_socket.connect(('localhost', 8000))

# Iniciar el hilo para recibir mensajes
hilo_recibir = threading.Thread(target=recibir_mensajes, args=(cliente_socket,))
hilo_recibir.start()
print ("<<Bienvenidos al Chat de Sistemas operativo>>\n")
while True:
    mensaje = input(">")
    cliente_socket.send(mensaje.encode("utf-8"))
    if mensaje=="exit":
        break
print ("Has salido del chat...")