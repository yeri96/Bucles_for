# !/usr/bin/python		# CON ESTA LINEA LE DECIMOS QUE LO QUE VIENE A CONTINUACION ES UN SCRIPT EN PYTHON
# coding:utf-8
import os, time		#IMPORTAMOS LAS LIBRERIAS

path_to_explore="./test/"

for root, dirs, files in os.walk(path_to_explore):
    for name in files:
        ruta_completa=os.path.join(root, name)
        print(ruta_completa)	# IMPRIMIMOS LA RUTA COMPLETA DE CADA ARCHIVO
        
        # FECHA DE ÚLTIMO ACCESO
        print time.ctime(os.path.getatime(ruta_completa))
        
		# FECHA DE ULTIMA MODIFICACIÓN
        print time.ctime(os.path.getmtime(ruta_completa))
