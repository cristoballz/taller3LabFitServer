import socket
import threading

clientes = []

def broadcast_mensaje(mensaje, origen_cliente):
    for cliente in clientes:
        if cliente != origen_cliente:
            cliente.send(mensaje)

def manejar_cliente(cliente_socket, cliente_direccion):
    while True:
        mensaje = cliente_socket.recv(1024).decode("utf-8")
        if not mensaje:
            break
        broadcast_mensaje(f"{cliente_direccion[0]}:{cliente_direccion[1]} dice: {mensaje}", cliente_socket)
        print (f"{mensaje}\n")

    # Si el cliente sale del bucle, eliminarlo de la lista de clientes
    clientes.remove(cliente_socket)
    cliente_socket.close()

# Crear el socket para el servidor
servidor_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
servidor_socket.bind(('localhost', 8000))
servidor_socket.listen(5)


print("Servidor iniciado en el puerto 8000, esperando a los usuarios..")

while True:
    cliente_socket, direccion = servidor_socket.accept()
    clientes.append(cliente_socket)

    print(f"Cliente conectado desde {direccion[0]}:{direccion[1]}")

    hilo_cliente = threading.Thread(target=manejar_cliente, args=(cliente_socket, direccion))
    hilo_cliente.start()