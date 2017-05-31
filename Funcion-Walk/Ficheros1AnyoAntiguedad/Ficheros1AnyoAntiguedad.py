# !/usr/bin/python		# CON ESTA LINEA LE DECIMOS QUE LO QUE VIENE A CONTINUACION ES UN SCRIPT EN PYTHON
# coding:utf-8
import os		#IMPORTAMOS LAS LIBRERIAS
import stat
import os, time

path_to_explore="./test/"	# RUTA DEL DIRECTORIO A EXPLORAR
total_size=0	# DEFINIMOS LA VARIABLE total_size

for root, dirs, files in os.walk(path_to_explore):
    for name in files:
        ruta_completa=os.path.join(root, name)
        total_size=total_size+os.stat(ruta_completa).st_size	# CALCULAMOS EL TAMAÑO DE CADA ARCHIVO

        if total_size > 100000 :	# SI PESA MÁS DE 1GB
            print (ruta_completa)
            print name,"Tamaño =",total_size,"k"
        else:
            print "No hay archivos de más de 1 GB"
