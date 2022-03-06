#!/usr/bin/python3

import time, datetime

from solar_module import SolarModule

if __name__ == '__main__':

	print('Hola')
	
	host = ''
	port = 2500
	
	# Llamada a la clase SolarModule para inicializar el socket
	obj_solar = SolarModule(host, port)
	
	# Mostramos el puerto de conexión
	print('[' + datetime.datetime.fromtimestamp(time.time()).strftime('%H:%M:%S') + '] Puerto de conexion:', port)
	# logging.info('[' + datetime.datetime.fromtimestamp(time.time()).strftime('%H:%M:%S') + '] Puerto de conexion:', port)
	
	# Llamada a la clase run del socket de SolarModule para que se inicie la conexión
	# e intercambio de conexión con el socket cliente que se le conecte
	obj_solar.run()
	
