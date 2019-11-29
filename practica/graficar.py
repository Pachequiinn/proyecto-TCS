import numpy
import matplotlib.pyplot as plt

def graficar(matriz_r, origen, tipo=0):

	if tipo < 0:
		tamanio = matriz_r.shape[0]
		convolucion = numpy.zeros(tamanio)
		for i in range(tamanio):
			convolucion[i] += matriz_r[i][0]
	else:
		tamanio = len(matriz_r)
		convolucion = matriz_r

	print(convolucion)
	inicio = -1*origen+1
	if tipo < 0:
		final = inicio + matriz_r.shape[0] - 1
	else:
		final = len(matriz_r) - 1
	print("Inicio: ",inicio, " Final: ",final)

	x = numpy.linspace(inicio, final, tamanio, endpoint=True)

	if(tipo==0):
		plt.title("Convolución finita")
	elif(tipo==1):
		plt.title("Convolución periódica")
	else:
		plt.title("Convolución circular")

	plt.grid(True)

	plt.stem(x, convolucion)
	plt.show()
