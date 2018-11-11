import random
import math

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
colores=['b', 'g', 'r', 'c', 'm', 'y', 'k', 'w']


def calc_dist(xi,xj,yi,yj):
    xx = xi-xj
    xx = xx*xx
    yy = yi-yj
    yy = yy*yy

    distancia = math.sqrt(xx+yy)
    return distancia



puntos =[
    [1, 1],
    [1, 3],
    [2, 4],
    [2, 2],
    [2, 3],
    [8, 6],
    [7, 4],
    [9, 6],
    [7, 5],
    [5, 8]
    ]


print(puntos)
for px, py in puntos:
    l=plt.plot(px, py, 'ko')
    plt.setp(l,markersize=5)


k=4

centroide = list()

for i in range(0, k):
    cx=np.random.randint(0,10)
    cy=np.random.randint(0,10)
    l=plt.plot(cx, cy,colores[i]+'x')
    plt.setp(l,markersize=15)
    centroide.append([cx, cy])
print("Centroides iniciales")
print(centroide)

iteracion = 1
for l in range(0, 10):

    distancias = list()
    pertenece = 0
    n_punto = 0
    asignacion = list()
    print("Calculo de distacias y asigacion a clusters")
    for x, y in puntos:
        dist_min = 1000
        n_centroide = 0
        for i, j in centroide:
            distancia = calc_dist(i, x, j, y)
            if dist_min > distancia:
                dist_min=distancia
                pertenece = n_centroide
            n_centroide += 1
        print("Punto:"+str(x)+","+str(y)+" pertenece:"+str(pertenece)+" dist_min="+str(dist_min))
        plt.plot(x, y,color=colores[pertenece],marker='o',markersize=5)
        asignacion.append([n_punto, pertenece])
        n_punto += 1
    #print(asignacion)
    for nc in range(0,k):
        sumx = 0
        sumy = 0
        puntos_cluster = 0
        for np, per in asignacion:
            if nc == per:
                i=0
                for x, y in puntos:
                    if np == i:
                        sumx += x
                        sumy += y
                        puntos_cluster +=1
                    i += 1
        if puntos_cluster:
            sumx = sumx/puntos_cluster
            sumy = sumy/puntos_cluster
        else:
            sumx = -1
            sumy = -1
        x = centroide[nc][0]
        y = centroide[nc][1]
        plt.plot([x, sumx], [y, sumy], color=colores[nc], linestyle=':')
        centroide[nc]=[sumx, sumy]
        pt = plt.plot(sumx, sumy, color=colores[nc], marker='+')
        plt.setp(pt, markersize=1*(iteracion+1))

    print("Nuevos centroides")
    print(centroide)
    iteracion += 1
    #plt.show()
plt.show()
print("OK")

