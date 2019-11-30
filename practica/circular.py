# -*- coding:utf-8 -*-

import numpy
import matplotlib.pyplot as plt
import sys

from graficar import graficar

def convolucion_circular(sh,osh,sg,osg):
	signal_h = sh
	signal_g = sg
	origin_signal_h = int(osh)
	origin_signal_g= int(osg)
	muestras_signal_h = signal_h.split(",")
	muestras_signal_g = signal_g.split(",")

	print(muestras_signal_h)
	print(muestras_signal_g)

	# Tamaño de las muestras
	tam_muestras_h = len(muestras_signal_h)
	tam_muestras_g = len(muestras_signal_g)

	# Busca el patron que se repite para ambas muestras
	periodo_h = 1
	control_h = 0
	for i in range(0, tam_muestras_h):
		# caso 1 numeros diferentes
		for j in range(1,tam_muestras_h):
			if muestras_signal_h[i] == muestras_signal_h[j] and control_h < 1:
				print("Ya encontre el patron de h(x)")
				print("Tiene periodo en: "+str(periodo_h+1))
				control_h += 1
			elif muestras_signal_h[i] != muestras_signal_h[j] and control_h < 1:
				periodo_h += 1
		# caso 2 numeros repetidos
	periodo_g = 1
	control_g = 0
	for i in range(0, tam_muestras_g):
		# caso 1 numeros diferentes
		for j in range(1,tam_muestras_g):
			if muestras_signal_g[i] == muestras_signal_g[j] and control_g < 1:
				print("Ya encontre el patron de g(x)")
				print("Tiene periodo en: "+str(periodo_g+1))
				control_g += 1
			elif muestras_signal_g[i] != muestras_signal_g[j] and control_g < 1:
				periodo_g += 1
		# caso 2 numeros repetidos
	# concatena2 = ""
	# for i in range(0, tam_muestras_g):
	# 	concatena = ""
	# 	for j in range(0,i+1):
	# 		concatena = concatena + str(muestras_signal_g[j])
	# 	# print(concatena)
	# 	concatena2 = concatena2 + str(muestras_signal_g[i])
	# 	print("comparando: "+concatena2+ " con " + concatena)
	# 	if concatena2 == concatena:
	# 		print("Encontre el patron es: " + concatena)


	# La posicion del origen  que tendra la matriz resultante sera
	# la suma de las posiciones antes de la posicion de origen de ambas muestras + 1
	position_origin_final = 1
	for i in range(0, tam_muestras_h):
		if i < origin_signal_h-1:
			position_origin_final += 1
	for i in range(0, tam_muestras_g):
		if i < origin_signal_g-1:
			position_origin_final += 1

	# variables para la operacion 1
	op_a = []
	op_b = [0.0]
	op_r = []
	# variables para la operacion 2
	op_2_a = []
	op_2_b = []
	op_2_r = []

	if periodo_h >= periodo_g:
		print("Se realizara la convolución de h(x)*g(x)")
		for i in range(0,periodo_g):
			for j in range(0,periodo_h):
				if i < periodo_g-1:
					op_a.append(float(muestras_signal_h[j])*float(muestras_signal_g[i]))
				else:
					op_b.append(float(muestras_signal_h[j])*float(muestras_signal_g[i]))
		# Agrega 0 al final de op_b
		op_a.append(0.0)
		print(op_a)
		print(op_b)
		for i in range(0,len(op_a)):
			op_r.append(float(op_a[i])+float(op_b[i]))
		# Agrega muestras adicionales de acuerdo al periodo mas pequeño
		for i in range(0,periodo_g):
			op_r.append(0.0)
		print(op_r)
		# Parte el arrelo y realiza la suma para dar la convolucion
		# Parte el arrelo y realiza la suma para dar la convolucion
		md_array = int(len(op_r)/2)
		for i in range(0,len(op_r)):
			if i < md_array:
				op_2_a.append(op_r[i])
			else:
				op_2_b.append(op_r[i])
		# Realiza la suma
		print(op_2_a)
		print(op_2_b)
		for i in range(0,len(op_2_a)):
			op_2_r.append(float(op_2_a[i])+float(op_2_b[i]))
		print(op_2_r)
		print("h(x)*g(x)= ")
		# print(array_res)
	else:
		print("Se realizara la convolución de g(x)*h(x)")
		for i in range(0,periodo_h):
			for j in range(0,periodo_g):
				if i < periodo_h-1:
					op_a.append(float(muestras_signal_g[j])*float(muestras_signal_h[i]))
				else:
					op_b.append(float(muestras_signal_g[j])*float(muestras_signal_h[i]))
		# Agrega 0 al final de op_b
		op_a.append(0.0)
		print(op_a)
		print(op_b)
		for i in range(0,len(op_a)):
			op_r.append(float(op_a[i])+float(op_b[i]))
		# Agrega muestras adicionales de acuerdo al periodo mas pequeño
		for i in range(0,periodo_h):
			op_r.append(0.0)
		print(op_r)
		# Parte el arrelo y realiza la suma para dar la convolucion
		md_array = int(len(op_r)/2)
		for i in range(0,len(op_r)):
			if i < md_array:
				op_2_a.append(op_r[i])
			else:
				op_2_b.append(op_r[i])
		# Realiza la suma
		print(op_2_a)
		print(op_2_b)
		for i in range(0,len(op_2_a)):
			op_2_r.append(float(op_2_a[i])+float(op_2_b[i]))
		print(op_2_r)
		print("g(x)*h(x)= ")

	print(position_origin_final)

	graficar(op_2_r, position_origin_final, muestras_signal_h, origin_signal_h, muestras_signal_g, origin_signal_g, tipo=2)

