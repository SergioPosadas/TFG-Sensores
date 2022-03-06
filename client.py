#!/usr/bin/python3

import socket, sys, time, datetime

class Client(object):
    """
        Creación de la clase cliente para probar la conexión con SolarModule
    """
    
    def __init__(self, host, port):
        """
            Creación del constructor init para inicializar el socket del cliente a través del puerto
        """
        # Asignación de los valores de las variables para iniciar y crear el socket del cliente
        self.host = host
        self.port = port
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                
        
    def run(self):
        """
            Método para conectar con el módulo y enviar mensajes
        """
        
        # Variable msg para intercambiar información
        msg = b'Hola'
        
        # Comando para conectarse con el socket del módulo cogiendo los valores de 
        # los argumentos introducidos al ejecutar el programa
        self.socket.connect((self.host, self.port))
                
        while True:
            # Una vez conectado con el socket del módulo, enviar el mensaje
            self.socket.sendall(msg)
                        
            # Al haber realizado la conexión guardamos la información recibida en la variable data
            data = self.socket.recv(1024)
            
            # Si se ha recibido información del socket del módulo, se va mostrando una enumeración
            # cada seguundo hasta que no se envíe nada o se corte la conexión
            if data:            
                print('[' + datetime.datetime.fromtimestamp(time.time()).strftime('%H:%M:%S') + '] Receiving data from SolarModules socket', )
                # logging.info('[' + datetime.datetime.fromtimestamp(time.time()).strftime('%H:%M:%S') + '] Data received from SolarModules socket:', msg)
                time.sleep(1)
                
            # Si no se recibe nada se corta la conexión creada
            else:
                self.socket.close()
                break
        
if __name__ == '__main__':
    
    print ('Hola')
    
    # Obtención de los valores introducidos en los argumentos del programa
    # para inicializar y conectar el socket del cliente
    host = sys.argv[1]
    port = int(sys.argv[2])
    
    # Llamada a la clase Client para inicializar el socket
    obj_client = Client(host, port)
    
    # Se muestra el puerto de conexión
    print('[' + datetime.datetime.fromtimestamp(time.time()).strftime('%H:%M:%S') + '] Conectado al puerto de SolarModule:', port)
    #logging.info('[' + datetime.datetime.fromtimestamp(time.time()).strftime('%H:%M:%S') + '] Conectado al puerto de SolarModule:', port)
    
    # Llamada a la clase run del socket de Client para que se inicie la conexión
    # e intercambio de información con el socket de SolarModule al que se conecta
    obj_client.run()
    

    
     
