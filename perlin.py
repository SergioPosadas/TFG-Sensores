#!/usr/bin/python3

import time, datetime, logging, noise

import numpy as np

import matplotlib.pyplot as plt

class PerlinPlain(object):
	"""
		Creación de la clase PerlinPlain para la generación del plano de perlin
	"""
	
	def __init__(self, m, n):
		"""
			Creación del constructor init para inicializar el plano para después rellenarlo
		"""
		
		# Asignación de los valores del ancho y el alto del plano para poder generarlo
		
		self.m = m
		self.n = n


	def run(self):
		"""
			Método para rellenar y ponderar los valores a unos reales de irradiancia
		"""
		
		# Creación de la variable shape que contendrá las dimensiones del plano con las variables (m,n)
		# y generación del plano con 0's para después generar el plano con ruido de perlin
		
		shape = (self.m,self.n)
		pl = np.zeros(shape)
		
		logging.info(pl)

		# Creación de las variables que se utilizarán para la generacion del ruido de perlin en el plano
		
		scale = 100.0						# Proporcion entre el plano dibujado y el real
		octaves = 6							# Número de nivel de detalle que se quiere tenga el ruido de perlin
		persistence = 0.75					# Número que determina cuánto contribuye una octava a la forma general
		lacunarity = 2.0					# Número que hace que la imagen sea mas heterogénea
		
		# Creación del ruido de perlin en el plano a través de dos bucles for y la funcion noise importada más arriba

		for i in range(shape[0]):
			for j in range(shape[1]):
				pl[i][j] = noise.pnoise2(i/scale,
										j/scale,
										octaves=octaves,
										persistence=persistence,
										lacunarity=lacunarity,
										repeatx=1000,
										repeaty=1000,
										base=100)			
		
		# Obtención de los valores máximos, mínimos, media, desviación y varianza del plano para obtener el dominio aleatorio del plano generado
		
		logging.info("Mostrando información del plano generado: ")
		
		maxim = np.amax(pl)
		logging.info("Maximun value is: " + str(maxim))
		
		minim = np.amin(pl)
		logging.info("Minimun value is: " + str(minim))
		
		med = np.mean(pl)
		logging.info("Medium value is: " + str(med))
		
		desv = np.std(pl)
		logging.info("El valor de la desviación típica es: " + str(desv))
		
		var = np.std(pl)
		logging.info("El valor de la varianza es: " + str(var))
		
		# El dominio aleatorio generado será el rango de valores entre el valor mínimo y el máximo de nuestro plano
		
		logging.info("El dominio aleatorio generado es: [" + str(minim) + ", " + str(maxim) + "]")
		
		# Dibujado del plano creado a través de matplotlib

		fig, ax = plt.subplots()		
		ax.imshow(pl)		
		plt.show()
		
		# Una vez que se sabe el dominio aleatorio, es necesario ponderarlo con el dominio "real" que hay en España, 
		# para saber la irradiación "real" de nuestro plano en el plano que hemos generado nuestros puntos se encuentran 
		# entre [-0,432342351 y 0,463847239], en el dominio que hemos elegido varían entre [2,47 y 4,65]
		# Por lo tanto necesitaremos hacer una ponderación guardando antes en unas variables los valores del dominio real
		# y creando la variable dominio donde guardaremos el dominio del plano ponderado
		
		dom = np.zeros(shape)
		mxdom = 4.65
		mndom = 2.47
		
		for i in range(shape[0]):
			for j in range(shape[1]):
				x = pl[i][j] - minim
				p = ((x * (mxdom - mndom))/(maxim - minim))
				r = mndom + p
				dom[i][j] = r		
		
		logging.info("Mostrando información del plano ponderado: ")		
		logging.info(dom)
		
		maximum = np.amax(dom)
		logging.info("El valor máximo es: " + str(maximum))
		
		minimum = np.amin(dom)
		logging.info("El valor mínimo es: " + str(minimum))
		
		media = np.mean(dom)
		logging.info("El valor de la media es: " + str(media))
		
		desviation = np.std(dom)
		logging.info("El valor de la desviación típica es: " + str(desviation))
		
		variance = np.std(dom)
		logging.info("El valor de la varianza es: " + str(variance))
		
		# El dominio ponderado será el rango de valores entre el valor mínimo y el máximo de nuestro plano ponderado
		
		logging.info("El dominio aleatorio generado es: [" + str(minimum) + ", " + str(maximum) + "]")
		
		# Obtención de los valores máximos, mínimos, media, desviación y varianza del plano 
		# ponderado para comprobar que se ha hecho bien e impresión del plano ponderado 
		
		fig, ax = plt.subplots()		
		ax.imshow(dom)		
		plt.show()
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
