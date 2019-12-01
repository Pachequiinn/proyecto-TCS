import numpy as np
from graficar import graficar

def espejo(signal, signal_o):
    signal_arr = np.array([1,-1,0,0.5,4,3,7])
    signal_origin = 4
    signal_reflejada = np.zeros(len(signal_arr))
    reflejada_origin = len(signal_arr)-signal_origin+1

    #print("Origen: ",signal_arr[signal_origin-1], "Tamanio: ", len(signal_arr))

    for i in range(len(signal_arr)):
        signal_reflejada[i] += signal_arr[len(signal_arr)-1-i]

    print("Original: ", signal_arr, " con origen ", signal_origin)
    print("Nueva: ", signal_reflejada, " con origen ", reflejada_origin)

    graficar(signal_reflejada, reflejada_origin, signal_arr, signal_origin)

def amplificacion(signal, k):
    signal_arr = np.array([1,-1,0,0.5,4,3,7])
    signal_origin = 5
    signal_amp = np.zeros(len(signal_arr))
    amplificada_origin = signal_origin

    print("Origen: ",signal_arr[signal_origin-1], "Tamanio: ", len(signal_arr))

    for i in range(len(signal_arr)):
        signal_amp[i] += signal_arr[i]*k

    print("Original: ", signal_arr)
    print("Nueva: ", signal_amp, " con origen ", amplificada_origin)

    graficar(signal_amp, amplificada_origin, signal_arr, signal_origin)

def desplazamiento(signal, signal_o, n0):

    signal_arr = np.array([1,-1,0,0.5,4,3,7])

    original_copy = np.array(signal_arr, copy = True)

    if(n0 < 0):
        if(-1*n0 >= signal_o):
            aux_zeros = np.zeros(-1*n0 - signal_o+1)
            signal_arr = np.append(aux_zeros, signal_arr)
            print("Valores arreglo: ", signal_arr)
            new_origin = 1
        else:
            new_origin = signal_o + n0

    else:
        if(n0 > len(signal_arr) - signal_o):
            #print("Resta: ",n0 - (len(signal_arr) - signal_o))
            aux_zeros = np.zeros(n0 - (len(signal_arr) - signal_o))
            signal_arr = np.append(signal_arr, aux_zeros)
            #print("Valores arreglo: ", signal_arr)
            new_origin = len(signal_arr)
            #print("Senial: ", signal_arr)
        else:
            new_origin = signal_o + n0            

    print("Anterior: ",original_copy, " Origen: ",signal_o)
    print("Secuencia: ",signal_arr, " Origen: ", new_origin)

    graficar(signal_arr, new_origin, original_copy, signal_o)


def diezmacion(signal, signal_o, k):

    signal_arr = np.array([2,5,3,0,7,9,-1,6,7,7,1])
    original_copy = np.array(signal_arr, copy = True)
    origina_o = signal_o

    posAux = signal_o
    aux = 1

    while(posAux < len(signal_arr)):
        if(aux != k):
            #print("A eliminar: ", signal_arr[posAux])
            signal_arr = np.delete(signal_arr, posAux)
            aux += 1
            #print("Eliminando: ", signal_arr)
        else:
            posAux += 1
            aux = 1

    #print("Primeros")

    posAux = signal_o - 2
    aux = 1

    #print("Senial: ", signal_arr, " origen: ",signal_o)

    while(posAux >= 0):        
        if(aux != k):
            #print("A eliminar: ", signal_arr[posAux])
            signal_arr = np.delete(signal_arr, posAux)
            aux += 1
            posAux -= 1
            signal_o -= 1
            #print("Eliminando: ", signal_arr)
        else:
            posAux -= 1
            aux = 1

    print("Anterior: ", original_copy, " origen: ", origina_o)
    print("Senial: ", signal_arr, "nuevoOrigen : ",signal_o)

    graficar(signal_arr, signal_o, original_copy, origina_o)

def intepolacionCero(signal, signal_o, k):

    signal_arr = np.array([1,2,3,4,5,6,7,8])
    size_original = len(signal_arr)

    if(signal_o == 1):
        new_o = 1
    else:
        new_o = signal_o + (signal_o-1)*(k-1)

    #print("Antiguo: ", signal_o ," Nuevo origen: ",new_o)

    posAux = 0
    i = 0
    j = k - 1

    inter_signal = np.zeros(size_original + (k-1)*(size_original - 1))
    #print("Tamanio nueva: ",len(inter_signal))

    while(posAux < len(inter_signal)):
        
        if(j != k - 1):
            j += 1
        else:
            inter_signal[posAux] += signal_arr[i]
            i += 1
            j = 0

        posAux += 1

    print("Vieja: ", signal_arr, " Origen: ", signal_o)
    print("Nueva: ",inter_signal, " Origen: ", new_o)
    
    graficar(inter_signal, new_o, signal_arr, signal_o)

def intepolacionEscalon(signal, signal_o, k):

    signal_arr = np.array([1,0,-1,2,3,0,8,0])
    size_original = len(signal_arr)

    if(signal_o == 1):
        new_o = 1
    else:
        new_o = signal_o + (signal_o-1)*(k-1)

    #print("Antiguo: ", signal_o ," Nuevo origen: ",new_o)

    posAux = 0
    i = 0
    j = k - 1

    inter_signal = np.zeros(size_original + (k-1)*(size_original - 1))
    #print("Tamanio nueva: ",len(inter_signal))

    while(posAux < len(inter_signal)):
        
        if(j != k - 1):
            inter_signal[posAux] += signal_arr[i-1]
            j += 1
        else:
            inter_signal[posAux] += signal_arr[i]
            i += 1
            j = 0

        posAux += 1

    print("Vieja: ", signal_arr, " Origen: ", signal_o)
    print("Nueva: ",inter_signal, " Origen: ", new_o)
    
    graficar(inter_signal, new_o, signal_arr, signal_o)    

def intepolacionLineal(signal, signal_o, k):

    signal_arr = np.array([1,0,-1,2,3,0,8,0])
    size_original = len(signal_arr)

    if(signal_o == 1):
        new_o = 1
    else:
        new_o = signal_o + (signal_o-1)*(k-1)

    #print("Antiguo: ", signal_o ," Nuevo origen: ",new_o)

    posAux = 0
    i = 0
    j = k - 1

    inter_signal = np.zeros(size_original + (k-1)*(size_original - 1))
    #print("Tamanio nueva: ",len(inter_signal))

    while(posAux < len(inter_signal)):
        
        if(j != k - 1):
            
            ni = abs(signal_arr[i-1] - signal_arr[i])/k

            if(signal_arr[i-1] > signal_arr[i]):
                ni *= -1

            inter_signal[posAux] += inter_signal[posAux-1]+ni
            j += 1
        else:
            inter_signal[posAux] += signal_arr[i]
            i += 1
            j = 0

        posAux += 1

    print("Vieja: ", signal_arr, " Origen: ", signal_o)
    print("Nueva: ",inter_signal, " Origen: ", new_o)
    
    graficar(inter_signal, new_o, signal_arr, signal_o)

#espejo(0, 0)
#print("")
#amplificacion(0, 2)
#print("")
#desplazamientoV = 0
#while(desplazamientoV != 100):
#    desplazamientoV = int(input("Ingresa el desplazamiento: "))
#    desplazamiento(0, 3, desplazamientoV)
diezmacion(1, 4, 8)
intepolacionCero(1, 8, 3)
intepolacionEscalon(1, 8, 2)
intepolacionLineal(1, 8, 4)