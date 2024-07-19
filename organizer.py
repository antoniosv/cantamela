from writefeat import *
import os, errno
from sys import *
from pprint import pprint
path = 'songs/'

def makeSongs(title):
# Taken from Hekki to create folder
    path = "features/" + title
    print path
    try:
        os.makedirs(path)
    except OSError, e:
        if e.errno != errno.EEXIST:
            raise

def makeHeader(title, headerpath):
    featfile = open(headerpath + ".dat", "w")
    print >> featfile, title
    featfile.close()

def fetchfeat(featname):
    # checar archivo featname y devolver la list estilo cubo
    cube = []
    #se guarda la matriz de los datos en cada fragmento y luego
    #se hace un append por cada matriz

    file = open("features/"+featname, "r")
    data = file.readlines()
    songname = data[0] 
    del data[0]
    fragment = 0
    while(1):
        size = data[0].split()
        row = int(size[0])
        col = int(size[1])
        longitud = (row*col)

        matrix = empty((row, col))
        r = 0
        c = 0

        del data[0] # se borra linea de dimensiones
        for line in data[0:longitud]:
            #print line
            matrix[r, c] = float(line)
            c += 1
            if c == col:
                c = 0
                r += 1 
        for line in data[0:longitud]:
            del data[0]
        #print "fin"
        cube.append(matrix) # se mete al cubo de fragmentos
        #print matrix

        if not data: break

    file.close()
#    print "se encontro ", songname
    return (songname, cube)

def makeDictionary():
    featpath = 'features/'
    featlog = dict()
#    featlog[featpath] = 0
#    featlog['uno'] = 1
#    featlog['zwei'] = 2
    for featitem in os.listdir(featpath):
        #para cada cancion, se saca su nombre visible y el "cubo" de features
        (displayname, cubo) = fetchfeat(featitem)
        print "Metiendo a ", displayname
        featlog[displayname] = cubo
    print "empieza diccionario"    
    pprint(featlog)
    return featlog

def query(songpath, jisho):
    recording = takeWav(songpath)
    sample = extractfeat(recording).X.T
    for mykey in jisho.keys():
        print mykey
        cube = jisho[mykey]
        for fragment in cube:
            officialSample = fragment
            score = compara(sample, officialSample)
            print score
            #print officialSample
        
def readDir():
    for dirname, dirnames, filenames in os.walk(path):
        for subdirname in dirnames:
            #print os.path.join(dirname, subdirname, " ~ ")
            #print subdirname
            headerpath = "features/" + subdirname
            makeHeader(subdirname, headerpath)
        for filename in filenames:
            #print os.path.join(dirname, filename)
            x = takeWav(os.path.join(dirname, filename))
            writeFeat(x, headerpath)
            
#readDir()
hashing = makeDictionary()

tuppie = query("ari_1.wav", hashing)
