# -*- coding:utf-8 -*-

import numpy
import matplotlib.pyplot as plt
import sys

from graficar import graficar

def convolucion_periodica(sh,osh,sg,osg):
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
	# El tamaño de la matriz A que debemos formar con cualquiera de las muestras es cuadrada, su tamaño n*n, donde n= la suma del tamaño de las dos muestras -1
	tam_matriz = (tam_muestras_h + tam_muestras_g)-1

	matriz_a = numpy.zeros((tam_matriz,tam_matriz))
	matriz_b = numpy.zeros((tam_matriz,1))
	matriz_r = numpy.zeros((tam_matriz,1))
	# La posicion del origen  que tendra la matriz resultante sera
	# la suma de las posiciones antes de la posicion de origen de ambas muestras + 1
	position_origin_final = 1
	for i in range(0, tam_muestras_h):
		if i < origin_signal_h-1:
			position_origin_final += 1
	for i in range(0, tam_muestras_g):
		if i < origin_signal_g-1:
			position_origin_final += 1

	# Llenado de matrices
	if tam_muestras_h >= tam_muestras_g:
		print("Se realizara la convolución de h(x)*g(x)")
		for col in range(0,tam_matriz):
			for fil in range(0,tam_matriz):
				if fil < tam_muestras_h and col == 0:
					matriz_a[fil,col] = muestras_signal_h[fil]
				elif fil > tam_muestras_h and col == 0:
					matriz_a[fil,col] = 0
				elif col > 0 and fil == 0:
					matriz_a[fil,col] = matriz_a[tam_matriz-1,col-1]
				elif col > 0 and fil > 0:
					matriz_a[fil,col] = matriz_a[fil-1 ,col-1]
		for col in range(0,1):
			for fil in range(0,tam_matriz):
				if fil < tam_muestras_g and col == 0:
					matriz_b[fil,col] = muestras_signal_g[fil]
				elif fil > tam_muestras_g and col == 0:
					matriz_b[fil,col] = 0
		array_res = []
		# multiplicacion de matrices
		for r in range(0,tam_matriz):
			for c in range(0,1):
				for k in range(0,tam_matriz):
					matriz_r[r,c] += matriz_a[r,k] *  matriz_b[k,c]
					array_res.append(matriz_a[r,k] *  matriz_b[k,c])
		print("h(x)*g(x)= ")
		# print(array_res)
	else:
		print("Se realizara la convolución de g(x)*h(x)")
		for col in range(0,tam_matriz):
			for fil in range(0,tam_matriz):
				if fil < tam_muestras_g and col == 0:
					matriz_a[fil,col] = muestras_signal_g[fil]
				elif fil > tam_muestras_g and col == 0:
					matriz_a[fil,col] = 0
				elif col > 0 and fil == 0:
					matriz_a[fil,col] = matriz_a[tam_matriz-1,col-1]
				elif col > 0 and fil > 0:
					matriz_a[fil,col] = matriz_a[fil-1 ,col-1]
		for col in range(0,1):
			for fil in range(0,tam_matriz):
				if fil < tam_muestras_h and col == 0:
					matriz_b[fil,col] = muestras_signal_h[fil]
				elif fil > tam_muestras_h and col == 0:
					matriz_b[fil,col] = 0
		array_res = []
		# multiplicacion de matrices
		for r in range(0,tam_matriz):
			for c in range(0,1):
				for k in range(0,tam_matriz):
					matriz_r[r,c] += matriz_b[r,k] *  matriz_a[k,c]
		print("g(x)*h(x)= ")
	#print(matriz_r)

	#Matriz de periodicidad
	if tam_matriz%2 == 0:	#par
		tam_matrizF = int(tam_matriz/2)
		matriz_rF1 = numpy.zeros((tam_matrizF,1))
		for r in range(0, tam_matrizF):
			for c in range(0, 1):
				matriz_rF1[r, c] = matriz_r[r, c]	
		matriz_rF2 = numpy.zeros((tam_matrizF,1))
		for r in range(0, tam_matrizF):
			for c in range(0, 1):
				matriz_rF2[r, c] = matriz_r[r + tam_matrizF, c]
		matriz_rF = numpy.zeros((tam_matrizF,1))
		for r in range(0, tam_matrizF):
			for c in range(0, 1):
				matriz_rF[r, c] = matriz_rF1[r, c] + matriz_rF2[r, c]
		print(matriz_rF)
	else:
		tam_matrizF = int((tam_matriz+1)/2)
		matriz_rF1 = numpy.zeros((tam_matrizF,1))
		for r in range(0, tam_matrizF):
			for c in range(0, 1):
				matriz_rF1[r, c] = matriz_r[r, c]
		matriz_rF2 = numpy.zeros((tam_matrizF,1))
		for r in range(0, tam_matrizF-1):
			for c in range(0, 1):
				matriz_rF2[r, c] = matriz_r[r + tam_matrizF, c]
		matriz_rF = numpy.zeros((tam_matrizF,1))
		for r in range(0, tam_matrizF):
			for c in range(0, 1):
				matriz_rF[r, c] = matriz_rF1[r, c] + matriz_rF2[r, c]
		print(matriz_rF)
	#matriz_rF = numpy.zeros((tam_matriz,1))
	print("Con origen en la posición: "+str(position_origin_final) + " con dato: " + str(matriz_rF[position_origin_final-1,0]))

	graficar(matriz_rF, position_origin_final, 1)
