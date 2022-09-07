#!/usr/bin/python3

from datetime import datetime

import time, datetime, logging

from solar_module import SolarModule

from perlin import PerlinPlain

if __name__ == '__main__':

	# Ponemos el nivel del log deseado
        logging.basicConfig(format='[%(levelname)s] %(asctime)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S', level=logging.DEBUG)
        
        logging.info('Hello!')
        
        host = ''
        port = 2500
        
        m = 20
        n = 20
        
        # Llamada a la clase SolarModule para inicializar el socket
        obj_solar = SolarModule(host, port)
        
        # Llamada a la clase PerlinPlain para crear el plano de irradiancia
        obj_perlin = PerlinPlain(m,n)
	
	    # Mensaje indicando que se está generando el plano
        logging.info('Waiting for the plain generation...')
	
	    # Llamada a la clase run de PerlinPlain para la ponderación de los 
	    # valores del plano creado con los reales de irradiancia
        obj_perlin.run()

        # Mensaje indicando que se está esperando una conexión
        logging.info('Waiting for a new conection...')

        # Llamada a la clase run del socket de SolarModule para que se inicie la conexión
        # e intercambio de conexión con el socket cliente que se le conecte
        obj_solar.run()
        
        
