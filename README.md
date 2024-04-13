# Proyecto Sockets

## Cómo funciona

Los scripts de Cliente.py y Servidor.py configuran un sistema básico de cliente-servidor usando sockets en Python. Este sistema permite que múltiples clientes envíen una solicitud a un servidor para obtener una lista de archivos en un directorio especificado. 

### Cliente.py
Este script se conecta al servidor para realizar dos operaciones principales: enviar un nombre de usuario y una ruta de directorio, y recibir una lista de archivos del directorio especificado. Estos son los pasos que sigue:

#### Argumentos del script:
Se utilizan argumentos de línea de comandos para especificar la dirección IP del servidor (host), el puerto (port), el nombre de usuario (nombre), y el número de veces (num) que el cliente intentará realizar la operación.

#### Conexión y comunicación:
El cliente crea un socket y se conecta al servidor usando la IP y el puerto especificados.
Una vez conectado, envía el nombre del usuario codificado en UTF-8.
Envía una ruta de directorio codificada en UTF-8 al servidor.
Espera recibir datos del servidor, los cuales serán la lista de archivos en el directorio especificado.
Imprime la lista de archivos recibida.
Este proceso se repite n veces según lo especificado en los argumentos del script.

#### Manejo de excepciones:
Se manejan errores como el tiempo de espera excedido (socket.timeout) y otros errores generales para asegurar que el cliente se maneje adecuadamente ante fallos de conexión o errores durante la transmisión de datos.

### Servidor.py
Este script se encarga de aceptar conexiones de múltiples clientes y responder a sus solicitudes:

#### Inicio del servidor:
El servidor se inicia en la IP y el puerto especificados, espera conexiones entrantes y, cuando acepta una conexión, inicia un nuevo hilo para manejar esa conexión específica.

#### Manejo de clientes:
Cuando un nuevo cliente se conecta, el servidor recibe primero el nombre del usuario.
Luego entra en un bucle donde espera recibir una ruta de directorio, procesa la solicitud usando la función list_files para obtener una lista de archivos en el directorio especificado, y envía esa lista al cliente.
Si no se reciben más datos (indicando que el cliente ha cerrado la conexión), el servidor rompe el bucle y cierra la conexión.

#### Función list_files:
Intenta listar los archivos en el directorio especificado y devuelve la lista.
Si el directorio no se encuentra, devuelve un mensaje de error.

#### Manejo de excepciones:
Se maneja la excepción ConnectionResetError que puede ocurrir si el cliente cierra la conexión abruptamente.
Interacción entre Cliente y Servidor


El cliente se conecta al servidor y envía su nombre y la ruta del directorio.
El servidor recibe esta información, procesa la solicitud, y devuelve la lista de archivos.
Este intercambio de información se realiza de forma segura y repetida mediante sockets y multihilos, lo que permite que el servidor maneje múltiples solicitudes simultáneamente.
