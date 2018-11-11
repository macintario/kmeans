import random
import math
import csv
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

k=7
ciclos=8

puntos = []

max = 0
with open("a1000.csv") as losDatos:
    datos = csv.reader(losDatos,delimiter=',')
    for renglon in datos:
        x = int(renglon[0])
        y = int(renglon[1])
        puntos.append([x,y])
        if x > max:
            max = x
        if y > max:
            max = y


print(puntos)
for px, py in puntos:
    l=plt.plot(px, py, 'ko')
    plt.setp(l,markersize=5)



centroide = list()

for i in range(0, k):
    cx=np.random.randint(0,max)
    cy=np.random.randint(0,max)
    l=plt.plot(cx, cy,colores[i]+'x')
    plt.setp(l,markersize=15)
    centroide.append([cx, cy])
print("Centroides iniciales")
print(centroide)

iteracion = 1
for l in range(0, ciclos):

    distancias = list()
    pertenece = 0
    n_punto = 0
    asignacion = list()
    print("Calculo de distacias y asigacion a clusters")
    for x, y in puntos:
        dist_min = max
        n_centroide = 0
        for i, j in centroide:
            distancia = calc_dist(i, x, j, y)
            if dist_min > distancia:
                dist_min=distancia
                pertenece = n_centroide
            n_centroide += 1
        #print("Punto:"+str(x)+","+str(y)+" pertenece:"+str(pertenece)+" dist_min="+str(dist_min))
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

