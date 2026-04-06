import time
import math

def factorial_iterativo(n):  #factorial iterativo
    resultado = 1
    for i in range(1, n + 1):
        resultado *= i  #multiplica desde 1 hasta n
    return resultado

def factorial_recursivo(n):  #factorial recursivo
    if n == 0 or n == 1:  #caso base
        return 1
    return n * factorial_recursivo(n - 1) #llamada recursiva

def calcular_media(lista): #calcula la media para el valor de n
    return sum(lista) / len(lista) #suma de tiempos entre las veces que se repite

def calcular_desviacion(lista): #calcula la desviacion para el valor de n
    media = calcular_media(lista)
    suma = 0
    for x in lista:
        suma += (x - media) ** 2
    return math.sqrt(suma / len(lista)) #aplicar formula de desviacion estandar

#main
if __name__ == "__main__":
    #valor de n
    #valores dados: 10,20,30,40,50,60,70,80,90,100,200,300,400,500,600,700
    n = int(input("Ingrese el valor de n: "))

    #resultados de cada tiempo
    tiempos_iterativo = []
    tiempos_recursivo = []

    for i in range(20): #20 repeticiones
        #Iterativo
        inicio = time.perf_counter()
        factorial_iterativo(n)
        fin = time.perf_counter()
        tiempo_iter = (fin - inicio) * 1000  #en milisegundos
        tiempos_iterativo.append(tiempo_iter)

        #Recursivo
        inicio = time.perf_counter()
        factorial_recursivo(n)
        fin = time.perf_counter()
        tiempo_rec = (fin - inicio) * 1000
        tiempos_recursivo.append(tiempo_rec)
    
    #Redondear listas a 8 decimales
    tiempos_iterativo = [round(t, 8) for t in tiempos_iterativo]
    tiempos_recursivo = [round(t, 8) for t in tiempos_recursivo]

    #calcular media
    media_iter = calcular_media(tiempos_iterativo)
    media_rec = calcular_media(tiempos_recursivo)
    #calcular desviacion
    desv_iter = calcular_desviacion(tiempos_iterativo)
    desv_rec = calcular_desviacion(tiempos_recursivo)

    #imprimir resultados
    print("--- Tiempos Iterativos ---")
    print("Iterativo:", tiempos_iterativo)
    print("\n--- Tiempos Recursivos ---")
    print("Recursivo:", tiempos_recursivo)
    print("\n--- m/d Iterativos ---")
    print("Media iterativo:", round(media_iter, 8))  #round redondea a 8 decimales
    print("Desviacion iterativo:", round(desv_iter, 8))
    print("\n--- m/d Recursivos ---")
    print("Media recursivo:", round(media_rec, 8))
    print("Desviacion recursivo:", round(desv_rec, 8))