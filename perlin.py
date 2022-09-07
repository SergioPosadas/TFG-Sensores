#!/usr/bin/python3

import time, datetime, logging

import numpy as np

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
		
		# Creación y generación del plano con la librería numpy con valores 
		# entre .0. y 1.0
		pl = np.random.random((self.m,self.n))
		
		logging.info(pl)

		# Falta pasarlo a Perlin y ponderar a valores reales de irradiancia o solo
		# ponderar a valores reales de irradiancia
