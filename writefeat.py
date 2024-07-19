from bregman.suite import *
from pylab import *
from numpy import *
from sys import *

# Este es para las matrices de features
def compara(x, y):
    UMBRAL = 0.000001
    D = distance.euc_normed(x, y)
    (row, col) = shape(D)
    distarray = open("distancia", "w")
    D.tofile(distarray, ",");
    distarray.close()
    dist = 0.0
    count = (row * col) * 1.0
    diag = 0.0
    count = min(row, col)
    total = 0.0
    for i in range(count):
        value = D[i, i]
        if not isnan(value):
            total += value
    dist = (total / count)
    #print 'Distancia: %g' % dist
    return (1.0 - dist)
#    return ( dist )

def writeFeat(x, name):
    p = default_feature_params()
    p['nhop'] = 2205
    p['feature'] = 'chroma'
    F = Features(x, p)
    if os.path.isfile(name+".dat"):
        prueba = open(name +".dat", "a")
    else:
        prueba = open(name +".dat", "w")
    (row, col) = shape(F.X.T)
    print >> prueba, '%d %d' % (row, col)
    for i in range(row):
        for j in range(col):
            print >> prueba, F.X.T[i, j]
    prueba.close()

def readFeat(filename):
    input = open(filename, 'r')
    data = input.readlines()
    size = data[0].split()
    row = int(size[0])
    col = int(size[1])
    print row, ",", col
    del data[0]
    matrix = empty((row, col))
    r = 0
    c = 0
    for d in data:
        matrix[r, c] = float(d)
        c += 1
        if c == col:
            c = 0
            r += 1 
    print matrix
    return matrix

def extractfeat(x):
    p = default_feature_params()
    p['nhop'] = 2205
    p['feature'] = 'chroma'
    F = Features(x,p)
#    G = Features(y,p)
    return F

# Este es para comparar features
def sim(F, G):
    UMBRAL = 0.000001
    D = distance.euc_normed(F.X.T, G.X.T)
    (row, col) = shape(D)
    dist = 0.0
    count = (row * col) * 1.0
    for i in range(row):
        total = 0.0
        for j in range(col):
            value = D[i, j]
            if value is not nan and value > UMBRAL:
#                print value, total
                total += value
#        print total
        dist += (total / count)
    return (1.0 - dist)

def makeCube(A, B, C):
    uno = extractfeat(A).X.T
    dos = extractfeat(B).X.T
    tres = extractfeat(C).X.T
    print uno
    cube = []
    cube.append(uno)
    cube.append(dos)
    cube.append(tres)
    for fragment in cube:
        print fragment

def takeWav(path):
    x, sr_x, fmt_x = wavread(path)
    return x

if __name__ == "__main__":
    try:
        file1 = argv[1]
        file2 = argv[2]
    except:
        file1 = "ari_1.wav"
        file2 = "cinco.wav"
    x, sr_x, fmt_x = wavread(file1) 
    y, sr_y, fmt_y = wavread(file2)
    z, sr_z, fmt_z = wavread("ari_2.wav")
    
    makeCube(x,y,z)

#extractfeat(x, y)
'''
    writeFeat(x, '1.feat');
    writeFeat(y, '2.feat');
    m1 = readFeat('1.feat.dat')
    m2 = readFeat('2.feat.dat')
    print compara(m1,m2)
'''
'''
matrix = readFeat('datos.dat')
print matrix
'''

''' 
hipotesis:
-reglones de la matriz de features se da por longitud de la pista
-Afecta mucho en los valores que tan alto es el volumen del audio   
-Columnas no varian


-> cantando el mismo fragmento 2 veces y comparandolos, da una similitud de 0.19
-> comparando la misma grabacion contra si misma da 0.36
-> comparando un fragmento con otro que nada que ver: 0.16
'''
