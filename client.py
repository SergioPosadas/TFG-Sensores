#!/usr/bin/python3

from datetime import datetime

import socket, sys, time, logging, json


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
        
        # Obtención del archivo json con el contenido del mensaje que se va a enviar a SolarModule
        with open("Request.json", "r", encoding='utf-8') as req:
        	self.request = json.load(req)
        	
        	# (Control) Mostrar por pantalla el archivo obtenido
        	logging.info(self.request)
             
        
    def run(self):
        """
            Método para conectar con el módulo y enviar mensajes
        """
                
        # Comando para conectarse con el socket del módulo cogiendo los valores de 
        # los argumentos introducidos al ejecutar el programa
        self.socket.connect((self.host, self.port))
                
        while True:
            # Una vez conectado con el socket del módulo, enviar el mensaje json codificado en bytes
            print(str(self.request))
            self.socket.sendall(bytes(str(self.request), 'utf-8'))
                        
            # Al haber realizado la conexión guardamos la información recibida en la variable data y la decodificamos
            data = self.socket.recv(1024)
                        
            # Si se ha recibido información del socket del módulo, se va mostrando una enumeración
            # cada seguundo hasta que no se envíe nada o se corte la conexión
            if data:            
                logging.info('Receiving data from SolarModules socket...')
                dat = data.decode()
                logging.info(dat)
                time.sleep(1)
                
            # Si no se recibe nada se corta la conexión creada
            else:
                self.socket.close()
                break
        

        
if __name__ == '__main__':
    
    # Ponemos el nivel del log deseado
    logging.basicConfig(format='[%(levelname)s] %(asctime)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S', level=logging.DEBUG)
    
    logging.info('Hola')
    
    # Obtención de los valores introducidos en los argumentos del programa
    # para inicializar y conectar el socket del cliente
    host = sys.argv[1]
    port = int(sys.argv[2])
    
    # Llamada a la clase Client para inicializar el socket
    obj_client = Client(host, port)
    
    # Se muestra el puerto de conexión
    logging.info('Connected to SolarModule...')
    
    # Llamada a la clase run del socket de Client para que se inicie la conexión
    # e intercambio de información con el socket de SolarModule al que se conecta
    obj_client.run()
    

    
     
