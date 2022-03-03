#!/usr/bin/python3

import time, datetime

from solar_module import SolarModule

if __name__ == '__main__':

	print('hola')
	
	host = ''
	port = 2500
	
	# Llamada a las clases SolarModule y cliente para inicializar ambos sockets
	obj_solar = SolarModule(host, port)
	obj_client = client(host, port)
	
	# Mostramos el puerto de conexión
	print('[' + datetime.datetime.fromtimestamp(time.time()).strftime('%H:%M:%S') + '] puerto de conexion:', port)
	# logging.info('[' + datetime.datetime.fromtimestamp(time.time()).strftime('%H:%M:%S') + '] puerto de conexion:', port)
	
	# Llamada a las clases run de cada socket para que inicien la conexión+
	# y el intercambio de conexión
	obj_solar.run()
	obj_client.run()
