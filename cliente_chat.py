import socket
import threading

def recibir_mensajes(servidor_socket):
    while True:
        mensaje = servidor_socket.recv(1024).decode("utf-8")        
        print(mensaje)

# Crear el socket para el cliente
cliente_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
cliente_socket.connect(('localhost', 8000))
nombre_usuario = ""

# Iniciar el hilo para recibir mensajes
hilo_recibir = threading.Thread(target=recibir_mensajes, args=(cliente_socket,))
hilo_recibir.start()
print ("\n<<Bienvenido al Chat de Sistemas operativos>>\n\n Aqui puedes escribir tus mensajes para comunicarte con los demas usuarios conectados al chat!\n\n Escribe '!help' para obtener ayuda sobre los comandos disponibles.\n")
nombre_usuario = input("Escriba su nombre de usuario para continuar: ")
while True:
    mensaje = input(nombre_usuario + ":") 
    cliente_socket.send((nombre_usuario + ": " + mensaje).encode("utf-8")) #el .encode encapsula todos los parametros anteriores al mismo ojo a los parentesis
    if mensaje=="!help":
        print("para salir del chat solo escribe 'exit' o 'salir'")
    if mensaje=="exit" or mensaje=="salir":
        print (nombre_usuario)
        break
print ("Has salido del chat...")