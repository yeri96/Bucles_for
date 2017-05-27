# !/usr/bin/python
# coding:utf-8
import os	# IMPORTAMOS LAS LIBRERIAS
 
path_to_explore="./SHIELD/"
 
# LISTAMOS SOLO LOS ARCHIVOS
for root, dirs, files in os.walk(path_to_explore):
    for name in files:
        print(name)
        
print "-------------------------------------"
# MOSTRAMOS SOLO LOS DIRECTORIOS
for root, dirs, files in os.walk(path_to_explore):
    for name in dirs:
        print(name)
