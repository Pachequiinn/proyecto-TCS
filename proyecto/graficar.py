import numpy
import matplotlib.pyplot as plt

def graficar(signal_res, origen, h, origenH, tipo=0):

    tamanio = len(signal_res)
    inicio = -1*origen+1
    final = inicio + tamanio - 1
    x = numpy.linspace(inicio, final, tamanio, endpoint=True)

    tamanioH = len(h)
    inicioH = -1*origenH+1
    finalH = inicioH + tamanioH - 1
    xH = numpy.linspace(inicioH, finalH, tamanioH, endpoint=True)
    
    fig, (senialOriginal, resGrafica) = plt.subplots(2)

    resGrafica.stem(x, signal_res, 'b', markerfmt='bo', use_line_collection=True)
    senialOriginal.stem(xH, h, 'g', markerfmt='go', use_line_collection=True)

    senialOriginal.grid(True)
    resGrafica.grid(True)

    for i,j in zip(xH,h):
        senialOriginal.annotate(str(j),xy=(i,j))

    for i,j in zip(x,signal_res):
        resGrafica.annotate(str(j),xy=(i,j))


    plt.show()