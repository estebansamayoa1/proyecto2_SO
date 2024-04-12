import socket
import os
import threading

def list_files(path):
    
    try:
        return '\n'.join(os.listdir(path))
    except FileNotFoundError:
        return "El directorio no fue encontrado."

def handle_client(conn, addr):
    """Función para manejar la conexión con cada cliente."""
    try:
        nombre = conn.recv(1024).decode('utf-8')  # Recibir el nombre del cliente
        print(f"Conectado por {addr}, Nombre: {nombre}")  # Mostrar el nombre del cliente
        while True:
            data = conn.recv(1024)
            if not data:
                break
            path = data.decode('utf-8')
            files_list = list_files(path)
            conn.sendall(files_list.encode('utf-8'))
    except ConnectionResetError as e:
        print(f"{e}. Conexión reseteada por el cliente {addr}, Nombre: {nombre}.")
    finally:
        conn.close()
        print(f"Conexión cerrada con {addr}, Nombre: {nombre}")

def server(ip, port):
    """Función para iniciar el servidor."""
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((ip, port))
        s.listen()
        print(f"Servidor escuchando en {ip}:{port}")

        while True:
            conn, addr = s.accept()
            client_thread = threading.Thread(target=handle_client, args=(conn, addr))
            client_thread.start()

if __name__ == "__main__":
    HOST = '172.20.10.5'
    PORT = 5577

    server(HOST, PORT)