#!/usr/bin/python3

from datetime import datetime

import numpy as np

import socket, sys, time, logging, json


class Sensor(object): 
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
            
            logging.info(self.REQUEST)
            	
            for i in range(shape[0]):
                for j in range(shape[1]):
                    self.REQUEST['X point'] = i           
                    self.REQUEST['Y point'] = j
                    
                    self.REQUEST['type'] = 'DATA'
                    self.REQUEST['message'] = 'response'
                    
                    logging.info("Message to send: " + str(self.REQUEST).replace("\'", "\""))
                    print("\n")
                    
                    self.socket.sendall(bytes((str(self.REQUEST).replace("\'", "\"")).encode()))
                    
                    # Función sleep para que haya un tiempo de espera entre petición y petición para no sobrecargar
                    # el servidor de peticiones y apreciar bien la peticion y la respuesta
                    
                    # time.sleep(2)                        
                    
                    # Al haber realizado la conexión guardamos la información recibida en la variable data y la decodificamos
                    
                    data = self.socket.recv(1024)
                        
                    # Si se ha recibido información del socket del módulo, se comprueba si se recibe el valor del punto y lo
                    # y lo muestra, o si por el contrario se ha enviado mal el punto, se vuelve a repetir. Si no se recibe nada
                    # se corta la conexión.
                    
                    if data:
                        logging.info('Receiving data from SolarModules socket...')
                        print("\n")
                        self.RESPONSE = json.loads(data)
                        if ((self.RESPONSE['Value']) and (self.RESPONSE['type'] == 'DATA')):
                    	    logging.info("Point value (" + str(self.RESPONSE.get("X point")) + ", " + str(self.RESPONSE.get("Y point")) + ") is: " + str(self.RESPONSE.get("Value")))
                    	    print("\n")
                    	
                    	# Si se recibe un REQUEST con mensaje repetir, se vuelve a enviar la solicitud del valor en ese punto
                    	    
                        elif self.RESPONSE['message'] == 'repeat':
                            logging.info("Bad sent request, we will repeat the REQUEST.")
                            self.REQUEST['X point'] = i
                            self.REQUEST['Y point'] = j
                            logging.info("Sending requested info...")
                            print("\n")     
                            	                           
                            self.socket.sendall(bytes((str(self.REQUEST).replace("\'", "\"")).encode()))
                            	    
                        else:
                            logging.info("Closing conection with module... Bye!")
                            print("\n")
                            connect.close()
                            self.socket.close()
                            break
        
        
if __name__ == '__main__':
    
    # Configuración del nivel del log deseado
    
    logging.basicConfig(format='[%(levelname)s] %(asctime)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S', level=logging.DEBUG)
    
    logging.info('Hellow')
    print("\n")
    
    # Obtención de los valores introducidos en los argumentos del programa
    # para inicializar y conectar el socket del sensor
    
    host = sys.argv[1]
    port = int(sys.argv[2])
    logging.info("Please, type the m and n values for the plain requests...")
    print("\n")
    logging.info("m value")
    m = int(input())
    print("\n")
    logging.info("n value")
    n = int(input())
    
    REQUEST = {'type':'QUERY','message':'request','port':'2500'}
    RESPONSE = {}
    
    # Llamada a la clase Sensor para inicializar el socket
    
    obj_sensor = Sensor(host, port, m, n, REQUEST, RESPONSE)
    
    # Se muestra el puerto de conexión
    
    logging.info('Connected to SolarModule...')
    print("\n")
    
    # Llamada a la clase run del socket de Sensor para que se inicie la conexión
    # e intercambio de información con el socket de SolarModule al que se conecta
    
    obj_sensor.run()
    

    
     
