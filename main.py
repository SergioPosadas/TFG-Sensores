#!/usr/bin/python3

from datetime import datetime

import time, datetime, logging

from Solar_Module import SolarModule

if __name__ == '__main__':

	# Configuración del nivel del log deseado
	
    logging.basicConfig(format='[%(levelname)s] %(asctime)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S', level=logging.DEBUG)
        
    logging.info('Hello!')
    print("\n")
    
    # Asignación de las variables que se utilizarán para creación del plano, conexión de sockets
    # y creación de los diferentes diccionarios utilizarán los mensajes para intercambio de información
    
    logging.info("Please, type the different values for the solar panel generation...")
    logging.info("- port (2500 by default)")
    port = int(input())
    print("\n")
    logging.info("- m value")
    m = int(input())
    print("\n")
    logging.info("- n value")
    n = int(input())
    print("\n")
    logging.info("- voltage")
    voltage = float(input())
    
    host = ''
    REQUEST = {}
    RESPONSE = {}
    
    REQUEST['type'] = 'QUERY'
    REQUEST['messsage'] = 'request'
    REQUEST['host'] = host
    REQUEST['port'] =  port
    REQUEST['m'] = m
    REQUEST['n'] = n
    REQUEST['voltage'] = voltage
        
    # Llamada a la clase SolarModule para inicializar el socket
    
    obj_solar = SolarModule(host, port, m, n, REQUEST, RESPONSE)
	
	# Mensaje indicando que se está generando el plano
	
    logging.info('Waiting for the plain generation...')
    print("\n")
	
	# Llamada a la clase run de PerlinPlain para la ponderación de los 
	# valores del plano creado con los reales de irradiancia
	
    obj_solar.run()

        
        
