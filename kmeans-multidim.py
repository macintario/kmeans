import numpy as np
from numpy import genfromtxt
import math

def calcula_distancia(x,y):
    distancia = 0
    for i in range(0, len(x)):
        d = x[i] -y[i]
        distancia = distancia + d*d

    distancia = math.sqrt(distancia)
    return distancia


################################
k = 7
iteraciones = 10
#################################


datos = genfromtxt("4x40.csv", delimiter=',')

dimensiones = datos.shape[1]
puntos = datos.shape[0]
##########################################
#Generamos k centroides
#########################################
print(datos)

max_mat = datos.max()
centroides = list()
for i in range(0, k):
    vector = np.random.randint(0, max_mat, dimensiones, np.int)
    centroides.append(vector)

print("############### CENTROIDES INICIALES")
print(centroides)
print("############### ITERACIONES ")

pertenece = dict()
for it in range(0, iteraciones):
    #Para cada centroide calcula la distancia a los nodos
    #Usa  la mínima para determinar la pertenencia al cluster
    min_dist = max_mat

    npunto = 0
    for pi in datos:
        min_dist = max_mat*2
        ncentroide = 0
        for ci in centroides:
            dist = calcula_distancia(ci, pi)
            if dist < min_dist:
                min_dist = dist
                pertenece[npunto] = ncentroide
            ncentroide += 1
        npunto += 1
    print(centroides)
    # recalculamos  ubicacion de centroide
    ncentroide = 0
    for ci in centroides:
        npunto = 0
        nuevo_centroide = np.zeros(dimensiones)
        numero_puntos= 0
        for pi in datos:
            if pertenece[npunto] == ncentroide:
                nuevo_centroide += pi
                numero_puntos += 1
            npunto += 1
        if numero_puntos > 0:
            nuevo_centroide = nuevo_centroide / numero_puntos
        else:
            nuevo_centroide = nuevo_centroide - 1

        centroides[ncentroide] = nuevo_centroide
        ncentroide += 1
    #print("########## centroides")
    #print(pertenece)


print("########## Final centroides")
print(centroides)