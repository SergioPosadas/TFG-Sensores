#!/usr/bin/env python3

from datetime import datetime

from mininet.log import setLogLevel, info
from mn_wifi.cli import CLI
from mn_wifi.net import Mininet_wifi
from mn_wifi.energy import Energy

import numpy as np

import socket, sys, time, json


"""
class Sensor(object):
     """  
        # Creación de la clase Mininet-Wifi para la conexión con Solar Module
"""
        
    def __init__(self, host, port, m, n, voltage, REQUEST, RESPONSE):           # ESTE CODIGO HAY QUE TRANSCRIBIRLO A LOS DIFERENTES CONSTRUCTORES DE NET, NODE, ETC
"""
            # Creación del constructor init para inicializar el socket de Mininet-Wifi a través del puerto
            # e intercambiar información del plano con el módulo
"""
        
        # Asignación de los valores de las variables para inicializar y crear el socket del sensor, así como de
        # la red de Mininet-Wifi.
        # Creación del diccionario que utilizarán los mensajes de intercambio de información.
        
        self.host = host
        self.port = port
        self.m = m
        self.n = n
        self.voltage = voltage
        self.REQUEST = REQUEST
        self.RESPONSE = RESPONSE
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
"""

def topology():                         # ESTO ES EL RUN DE PYTHON
    """
            Creación de la topología del Sensor IoT
    """
    
    net = Mininet_wifi()   # no es necesario iot_module
    # iot_module: fakelb or mac802154_hwsim
    # mac802154_hwsim is only supported from kernel 4.18
    # mac80211_hwsim by default

    info("*** Creating nodes\n")            # Cambiar la funcion para añadir también panel solar
    net.addSolarSensors('sensor1', ip6='2001::1/64', voltage=3.7, panid='0xbeef')
    # ip6='2001::1/64' se puede con ip4 - m=300, n=300
    # net.addSolarSensors('sensor2', ip6='2001::2/64', voltage=3.7, panid='0xbeef')
    # net.addSolarSensors('sensor3', ip6='2001::3/64', voltage=3.7, panid='0xbeef')

    info("*** Configuring nodes\n")
    net.configureNodes()

    info("*** Starting network\n")
    net.build()

    info("*** Running CLI\n")
    CLI(net)

    info("*** Stopping network\n")
    net.stop()
 
"""
    def run(self):                          # ESTE CODIGO VA EN ENERGY, DALE VUELTAS PARA TRANSCRIBIRLO BIEN
""" 
            # Método para conectar con el módulo e intercambiar la información necesaria para Mininet-Wifi
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
                    
                    self.REQUEST['Type'] = 'DATA'
                    self.REQUEST['Message'] = 'response'
                    
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
                        logging.info(self.RESPONSE)
                        if ((self.RESPONSE['Value']) and (self.RESPONSE['type'] == 'DATA')):
                	        logging.info("Point value (" + str(self.RESPONSE.get("X point")) + ", " + str(self.RESPONSE.get("Y point")) + ") is: " + str(self.RESPONSE.get("Value")))
                	        print("\n")
                    	        
                  	    # Si se recibe un REQUEST con mensaje repetir, se vuelve a enviar la solicitud del valor en ese punto
                    	    
                        elif self.RESPONSE['Message'] == 'repeat':
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
"""            


if __name__ == '__main__':
    
    # Configuración del nivel del log deseado
    # logging.basicConfig(format='[%(levelname)s] %(asctime)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S', level=logging.DEBUG)
    setLogLevel('info') # este mejor
    
    topology()
    
"""
    # ESTE CODIGO HAY QUE TRANSCRIBIRLO A LOS ARCHIVOS NET, NODE, ETC
    
    logging.info('Hellow')
    print("\n")
    
    # Obtención de los valores introducidos en los argumentos del programa
    # para inicializar y conectar el socket del sensor
    
    logging.info("Please, type the different values for the solar panel requests...")
    
    logging.info("- Host (localhost)")
    host = input()               # Dirección IP a dónde se realizará la conexión con el panel solar
    print("\n")
    
    logging.info("- Port (2500 by default)")
    port = int(input())          # Puerto donde se realizará la conexión con el panel solar
    print("\n")
    
    logging.info("- M value (cm - 300 recommended)")
    m = int(input())             # "Longitud" del panel solar para guardar los valores de la irradiancia en cada punto del panel en nuestro módulo Mininet-WiFi
    print("\n")
    
    logging.info("- N value (cm - 300 recommended)")
    n = int(input())             # "Altura" del panel solar para guardar los valores de la irradiancia en cada punto del panel en nuestro módulo Mininet-WiFi
    print("\n")
    
    
    # logging.info("- Voltage")
    # voltage = float(input())
    # print("\n")
    
    
    REQUEST = {}
    RESPONSE = {}
    
    REQUEST['Type'] =  'QUERY'
    REQUEST['Message'] = 'request'
    REQUEST['Host'] = host
    REQUEST['Port'] =  port
    REQUEST['M'] = m
    REQUEST['N'] = n
    # REQUEST['Voltage'] = voltage
    
    logging.info("Showing REQUEST message: " + str(REQUEST))
    
    # Llamada a la clase Mininet-Wifi para inicializar la aplicación
    
    obj_sensor = MininetWifi(host, port, m, n, REQUEST, RESPONSE) # quitarlo
    
    # Se muestra el puerto de conexión
    
    logging.info('Connected to Solar Module...')
    print("\n")
    
    # Llamada a la clase run del socket del sensor Mininet-Wifi para que se inicie la conexión
    # e intercambio de información con el socket de SolarModule al que se conecta
    
    obj_sensor.run()
""" 
   
   
   
   
   
   
   
   
   
   
   
   
