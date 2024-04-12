import argparse
import socket

def client(ip, port, nombre, n):
    """Función para conectar el cliente al servidor y enviar/recibir datos múltiples veces."""
    for _ in range(n):
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.settimeout(10) 
                s.connect((ip, port))
                s.sendall(nombre.encode('utf-8'))  
                
                path = "/Users/nickolasnolte"
                if path.lower() == 'salir':
                    break 
                
                s.sendall(path.encode('utf-8'))  
                data = s.recv(1024) 
                print("Archivos en el directorio:", data.decode('utf-8'))
                
        except socket.timeout:
            print("La conexión ha superado el tiempo máximo de espera.")
        except Exception as e:
            print(f"Error: {e}")
            break  

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Cliente TCP para enviar y recibir datos del servidor.')
    parser.add_argument('host', type=str, help='La dirección IP del host.')
    parser.add_argument('port', type=int, help='El puerto del servidor.')
    parser.add_argument('nombre', type=str, help='El nombre del usuario.')
    parser.add_argument('-n', '--num', type=int, default=1, help='Número de veces que desea realizar la operación.')

    args = parser.parse_args()

    client(args.host, args.port, args.nombre, args.num)
