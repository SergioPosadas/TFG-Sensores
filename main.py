#!/usr/bin/python3

from datetime import datetime

import time, datetime, logging

from Solar_Module import SolarModule

# from perlin import PerlinPlain

if __name__ == '__main__':

	# Ponemos el nivel del log deseado
    logging.basicConfig(format='[%(levelname)s] %(asctime)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S', level=logging.DEBUG)
        
    logging.info('Hello!')
    
    # Asignación de las variables que se utilizarán para creación del plano, conexión de sockets
    # y creación de los diferentes diccionarios utilizarán los mensajes para intercambio de información
    
    m = 1000
    n = 1000
    host = ''
    port = 2500
    REQUEST = {'type':'QUERY','message':'request','port':'2500'}
    RESPONSE = {}
        
    # Llamada a la clase SolarModule para inicializar el socket
    obj_solar = SolarModule(host, port, m, n, REQUEST, RESPONSE)
	
	# Mensaje indicando que se está generando el plano
    logging.info('Waiting for the plain generation...')
	
	# Llamada a la clase run de PerlinPlain para la ponderación de los 
	# valores del plano creado con los reales de irradiancia
    obj_solar.run()

        
        
