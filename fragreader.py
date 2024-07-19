#! /usr/bin/python
from numpy import *
import sys

file = open("rola.dat", "r")
songname = file.readline()
fragment = 0
print "Datos de la cancion:" ,songname
while 1:
   data = file.readline()
   size = data.split(' ')
   if len(size) >=2:
      row = int(size[0])
      col = int(size[1])
      fragment+=1   
      print "Fragmento",fragment
      print "Tamanio: [",row, "," ,col,"]"
   else:
#      matrix = empty((row,col))
 #     print matrix
  #    r = 0
   #   c = 0
    #  for d in data:
     #    matrix[r,c] = d
      #   c+=1
       #  if c == col:
        #    c = 0
         #   r += 1
      print matrix
   if not data: break
file.close()
