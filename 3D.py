from math import sqrt #from time import time

def devuelveDist(x, y):
    return sqrt(x ** 2 + y ** 2)

def devuelveZs(rX, rY, f): # z = f(x, y) 
    zs = []

    for x in range(rX):
        for y in range(rY):
            zs.append(round(f(x, y), 2))

    return zs

def pintaZ(rX, rY, f): # lento # t = time()
    zs = devuelveZs(rX, rY, f) # print("tardo", round(time() - t, 2), "s")
    
    for x in range(rX):
        for y in range(rY):
            nElem = 100 * x + y

            print("nElem =", nElem, ", x =", x, ", y =", y,
                  ", z =", zs[nElem]) # lento
            
#PROBADOR # lento
#print(devuelveZs(100, 100, devuelveDist)) 
#pintaZ(100, 100, devuelveDist)


