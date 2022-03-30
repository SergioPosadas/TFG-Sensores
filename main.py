#!/usr/bin/python3

import time, datetime, logging

from solar_module import SolarModule

if __name__ == '__main__':

	# Ponemos el nivel del log deseado
        logging.basicConfig(format='[%(levelname)s] %(asctime)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S', level=logging.DEBUG)
        
        logging.info('Hello!')
        
        host = ''
        port = 2500
        
        # Llamada a la clase SolarModule para inicializar el socket
        obj_solar = SolarModule(host, port)
        
        # Mensaje indicando que se está esperando una conexión
        logging.info('Waiting for a new conection...')
        
        # Llamada a la clase run del socket de SolarModule para que se inicie la conexión
        # e intercambio de conexión con el socket cliente que se le conecte
        obj_solar.run()
        
        
	
