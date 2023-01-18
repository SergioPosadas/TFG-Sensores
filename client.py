#!/usr/bin/python3

from datetime import datetime

import numpy as np

import socket, sys, time, logging, json


class Client(object): # Sensor
    """
        Creación de la clase cliente para probar la conexión con SolarModule (Cambiar el nombre a sensor)
    """
    
    def __init__(self, host, port, m, n, REQUEST, RESPONSE):
        """
            Creación del constructor init para inicializar el socket del sensor a través del puerto
            e intercambiar información del plano con el módulo
        """
        
        # Asignación de los valores de las variables para iniciar, crear el socket del cliente 
        # Y creación del diccionario que utilizarán los mensajes de intercambio de información
        self.host = host
        self.port = port
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.REQUEST = REQUEST
        self.RESPONSE = RESPONSE
        self.m = m
        self.n = n            
        
    def run(self):
        """
            Método para conectar con el módulo y enviar mensajes
        """
                
        # Comando para conectarse con el socket del módulo cogiendo los valores de 
        # los argumentos introducidos al ejecutar el programa
        self.socket.connect((self.host, self.port))
        
        # Generación de un array del mismo tamaño que el plano para poder realizar la solicitud del
        # valor de la irradiancia en el punto del plano solicitado
        shape = (self.m, self.n)
                        
        while True:
            # Una vez conectado con el socket del módulo, enviar el mensaje json codificado en bytes
            #print(str(self.request))
            logging.info(self.REQUEST)
            	
            for i in range(shape[0]):
                for j in range(shape[1]):
                    self.REQUEST['X point'] = i           
                    self.REQUEST['Y point'] = j
                
                    logging.info(str(self.REQUEST).replace("\'", "\"").encode())
                    
                    self.socket.sendall(bytes((str(self.REQUEST).replace("\'", "\"")).encode()))                        
                    
                    # Al haber realizado la conexión guardamos la información recibida en la variable data y la decodificamos
                    data = self.socket.recv(1024)
                        
                    # Si se ha recibido información del socket del módulo, se comprueba si se recibe el valor del punto y lo
                    # y lo muestra, o si por el contrario se ha enviado mal el punto, se vuelve a repetir. Si no se recibe nada
                    # se corta la conexión.
                    
                    if data:            
                        logging.info('Receiving data from SolarModules socket...')
                        self.RESPONSE = data.decode()
                        if self.RESPONSE['Value']:
                    	    logging.info("Point value (" + str(self.RESPONSE.get("X point")) + ", " + str(self.RESPONSE.get("Y point")) + ") is: " + str(self.RESPONSE.get("Value")))
                    	    
                        elif self.RESPONSE['message'] == 'repeat':
                            logging.info("Bad sent request, pls repeat it.")
                            for i in range(shape[0]):                                
                                for j in range(shape[1]):
                            	    self.REQUEST['X point'] = i
                            	    self.REQUEST['Y point'] = j
                            	    logging.info("Sending requested info...")                            
                            	    self.socket.sendall(bytes((str(self.REQUEST).replace("\'", "\"")).encode()))
                            	    
                        else:
                            logging.info("Closing conection with module... Bye!")
                            connect.close()
                            self.socket.close()
                            break
                    
                    '''
                    # Si no se recibe nada se corta la conexión creada
                    else:
                        logging.info("Closing conection with module... Bye!")
                        connect.close()
                        self.socket.close()
                        break
                    '''
        
        
if __name__ == '__main__':
    
    # Ponemos el nivel del log deseado
    logging.basicConfig(format='[%(levelname)s] %(asctime)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S', level=logging.DEBUG)
    
    logging.info('Hellow')
    
    # Obtención de los valores introducidos en los argumentos del programa
    # para inicializar y conectar el socket del cliente
    host = sys.argv[1]
    port = int(sys.argv[2])
    m = 1000
    n = 1000
    REQUEST = {'type':'QUERY','message':'request','port':'2500'}
    RESPONSE = {}
    
    # Llamada a la clase Client para inicializar el socket
    obj_client = Client(host, port, m, n, REQUEST, RESPONSE) #Sensor
    
    # Se muestra el puerto de conexión
    logging.info('Connected to SolarModule...')
    
    # Llamada a la clase run del socket de Client para que se inicie la conexión
    # e intercambio de información con el socket de SolarModule al que se conecta
    obj_client.run()
    

    
     
