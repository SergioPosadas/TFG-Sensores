import socket
import sys
import logging
import time
import datetime

class SolarModule():
    """ 
    Creación de la clase SolarModule para probar el modulo a implementar 
    """
    
    host = ''
    port = 2500
    socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)   
    #creación de las variables que se utilizarán en el constructor y en el método run
    
    def __init__(p, s):       
    #creación del constructor init para inicializar el socket a través del puerto
        
        self.port = p         
        self.socket = s
        #asignación de los valores correspondientes a las variables para poner el socket a escuchar
    
    
         
    def run(self):
    #método para poner al socket a escuchar conexiones
    
        self.s.bind((host, self.p))
        #comando para indicarle al socket en qué puerto escuchar las conexiones
        self.s.listen(1)
        #comando para que el socket acepte conexiones, el 1 indica que sólo se aceptará una conexión
        while True:
            connect, address = self.s.accept()
            #comando para estar a la espera de conexiones, devolviendo la conexión del cliente (guardada en connect) y la dirección (host y puerto) de dicha conexión         
            logging.info('[' + datetime.datetime.fromtimestamp(time.time()).strftime('%H:%M:%S') + '] conectado a', address)
            #mensaje que informa sobre la dirección del cliente que se ha conectado, de momento solo saca la hora y la fecha
            break
            
        print('[' + datetime.datetime.fromtimestamp(time.time()).strftime('%H:%M:%S') + '] adios')
        self.s.close()
        #cierre de la conexión
        

