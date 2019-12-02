import tkinter as tk
import numpy as np
import operacionesDiscretas as opeDis

def leer_hX():
    print("Valores obtenidos: ",signal_h.get())
    print("Origen ingreado: ",origin_signal_h.get())

    muestras_signal_h = signal_h.get().split(",")
    print(muestras_signal_h)
    tam_muestras_h = len(muestras_signal_h)
    signal_h_arr = np.zeros(tam_muestras_h)

    for i in range(tam_muestras_h):
        signal_h_arr[i] += float(muestras_signal_h[i])

    print("Obtenida: ",signal_h_arr, " de tipo ", type(signal_h_arr))
    print("Origen: ", int(origin_signal_h.get()))

    return signal_h_arr, int(origin_signal_h.get())

def realizar_amplificacion():
    signal_arr, origen = leer_hX()
    opeDis.amplificacion(signal_arr, origen, int(factorAmplificacion.get()))

def realiar_reflejo():
    signal_arr, origen = leer_hX()
    opeDis.espejo(signal_arr, origen)

def realizar_desplazamiento():
    signal_arr, origen = leer_hX()
    opeDis.desplazamiento(signal_arr, origen, int(valorDesplazamiento.get()))

def realizar_interpolacionZero():
    signal_arr, origen = leer_hX()
    opeDis.interpolacionCero(signal_arr, origen, int(factorInterpolacion.get()))

def realizar_interpolacionEscalon():
    signal_arr, origen = leer_hX()
    opeDis.interpolacionEscalon(signal_arr, origen, int(factorInterpolacion.get()))

def realizar_interpolacionLineal():
    signal_arr, origen = leer_hX()
    opeDis.interpolacionLineal(signal_arr, origen, int(factorInterpolacion.get()))

def realizar_diezmacion():
    signal_arr, origen = leer_hX()
    opeDis.diezmacion(signal_arr, origen, int(factorDiezmacion.get()))

if __name__ == "__main__":
    frame = tk.Tk()
    frame.title("Proyecto: Operaciones básicas")
    
    tk.Label(frame, text="Proyecto: Operaciones básicas", font=("Helvetica", 16)).grid(row=0, column=1)
    tk.Label(frame,text="Ingresa la señal h(x) a modificar:").grid(row=1, sticky=tk.W, pady=4)
    tk.Label(frame,text="Ingresa posición de origen de h(x):").grid(row=2, sticky=tk.W, pady=4)
    tk.Label(frame,text="Valor de amplificación:").grid(row=3, sticky=tk.W, pady=4)
    tk.Label(frame,text="Valor de desplazamiento:").grid(row=4, sticky=tk.W, pady=4)
    tk.Label(frame,text="Factor k de interpolación:").grid(row=5, sticky=tk.W, pady=4)
    tk.Label(frame,text="Factor k de diezmación:").grid(row=8, sticky=tk.W, pady=4)

    signal_h = tk.Entry(frame)
    origin_signal_h = tk.Entry(frame)
    factorAmplificacion = tk.Entry(frame)
    valorDesplazamiento = tk.Entry(frame)
    factorInterpolacion = tk.Entry(frame)
    factorDiezmacion = tk.Entry(frame)

    signal_h.grid(row=1, column=1)
    origin_signal_h.grid(row=2, column=1)
    factorAmplificacion.grid(row=3, column=1)
    valorDesplazamiento.grid(row=4, column=1)
    factorInterpolacion.grid(row=5, column=1)
    factorDiezmacion.grid(row=8, column=1)

    tk.Button(frame, text="Amplificar/Atenuar h(x)", command=realizar_amplificacion).grid(row=3, column=2, sticky=tk.W, pady=4)
    tk.Button(frame, text="Desplazar h(x)", command=realizar_desplazamiento).grid(row=4, column=2, sticky=tk.W, pady=4)
    tk.Button(frame, text="Interpolar a cero h(x)", command=realizar_interpolacionZero).grid(row=5, column=2, sticky=tk.W, pady=4)
    tk.Button(frame, text="Interpolación escalón h(x)", command=realizar_interpolacionEscalon).grid(row=6, column=2, sticky=tk.W, pady=4)
    tk.Button(frame, text="Interpolación lineal h(x)", command=realizar_interpolacionLineal).grid(row=7, column=2, sticky=tk.W, pady=4)
    tk.Button(frame, text="Diezmar h(x)", command=realizar_diezmacion).grid(row=8, column=2, sticky=tk.W, pady=4)


    tk.mainloop()