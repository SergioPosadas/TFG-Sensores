"""
   Mininet-WiFi: A simple networking testbed for Wireless OpenFlow/SDWN!
   @author: Ramon Fontes (ramonrf@dca.fee.unicamp.br)
"""

# PARTE DE client.py
from datetime import datetime

import numpy as np

import socket, sys, time, json
#

from threading import Thread as thread
from time import sleep, time

from mininet.log import error


class Energy(object):

    thread_ = None
    cat_dev = 'cat /proc/net/dev | grep {} |  awk \'{}\''

    def __init__(self, nodes):
        self.start_simulation = 0
        Energy.thread_ = thread(target=self.start, args=(nodes,))
        Energy.thread_.daemon = True
        Energy.thread_._keep_alive = True
        Energy.thread_.start()

    def start(self, nodes):
        self.start_simulation = self.get_time()

        for node in nodes:
            for intf in node.wintfs.values():
                intf.rx, intf.tx = 0, 0

        try:
            while self.thread_._keep_alive:
                sleep(1)  # set sleep time to 1 second
                for node in nodes:
                    for intf in node.wintfs.values():
                        intf.consumption = self.getTotalEnergyConsumption(intf)
        except:
            error("Error with the energy consumption function\n")

    @staticmethod
    def get_time():
        return time()

    def get_duration(self):
        return self.get_time() - self.start_simulation

    def get_cat_dev(self, intf, col):
        p = '{print $%s}' % col
        return int(intf.cmd(Energy.cat_dev.format(intf.name, p)))

    def get_rx_packet(self, intf):
        rx = self.get_cat_dev(intf, 3)
        if rx != intf.rx:
            intf.rx = rx
            return True

    def get_tx_packet(self, intf):
        tx = self.get_cat_dev(intf, 11)
        if tx != intf.tx:
            intf.tx = tx
            return True

    def getState(self, intf):
        if self.get_rx_packet(intf):
            return 'rx'
        elif self.get_tx_packet(intf):
            return 'tx'
        return 'idle'

    def get_energy(self, intf, factor):
        return self.get_duration() * factor * intf.voltage

    def getTotalEnergyConsumption(self, intf):
        state = self.getState(intf)
        # energy to decrease = time * voltage (mA) * current
        if state == 'idle':
            return self.get_energy(intf, 0.273)
        elif state == 'tx':
            return self.get_energy(intf, 0.380)
        elif state == 'rx':
            return self.get_energy(intf, 0.313)
        elif state == 'sleep':
            return self.get_energy(intf, 0.033)
        return 0
    
    # PARTE PEGADA DE client.py
    def run(self):                          # ESTE CODIGO VA EN ENERGY, DALE VUELTAS PARA TRANSCRIBIRLO BIEN
        """
            Método para conectar con el módulo e intercambiar la información necesaria para Mininet-Wifi
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
    
    # CREACION DEL CALCULO DE LA ENERGIA GENERADA
    
    def getTotalEnergyGeneration(self, m, n, irradiance, medium, ):
        """
        state = self.getState(intf)
        # energy to decrease = time * voltage (mA) * current
        if state == 'idle':
            return self.get_energy(intf, 0.273)
        elif state == 'tx':
            return self.get_energy(intf, 0.380)
        elif state == 'rx':
            return self.get_energy(intf, 0.313)
        elif state == 'sleep':
            return self.get_energy(intf, 0.033)
        return 0
        """
    
        # Cálculo de la dimensión del panel solar
        dimension = self.RESPONSE.get("m") * self.RESPONSE.get("n")
                                
        # Cálculo de la irrandiancia solar recogida por el panel solar en cada punto
        power = self.RESPONSE.get("Value") * dimension
                                
        # Cálculo del valor de la irradiancia media del panel solar
        medium_irradiance = self.RESPONSE.get("Medium irradiance") * dimension
    
        """
        # Cálculo del voltage en cada punto del panel solar
        spvolt = power / "¿INTENSIDAD?"
                                
        # Cálculo del voltage medio del panel solar
        spmvolt = medium irradiance / "¿INTENSIDAD MEDIA?"
        """
    
    def shutdown_intfs(self, node):
        # passing through all the interfaces
        # but we need to consider interfaces separately
        for wlan in node.params['wlans']:
            self.ipLink(wlan)

    def ipLink(self, intf):
        "Configure ourselves using ip link"
        self.cmd('ip link set {} down'.format(intf.name))
