# !/usr/bin/python		# CON ESTA LINEA LE DECIMOS QUE LO QUE VIENE A CONTINUACION ES UN SCRIPT EN PYTHON
# coding:utf-8
import os		#IMPORTAMOS LAS LIBRERIAS
 
path_to_explore="./SHIELD/"
total_size=0
        
# MOSTRAMOS LA RUTA DE TODO
for root, dirs, files in os.walk(path_to_explore):		# UTILIZAMOS LA FUNCION WALK PARA RECORRER TODOS LOS SUBDIRECTORIOS DE ./SHIELD/
    for name in files:
        name_path=os.path.join(root, name)
        print(name_path) ,
        print os.stat(name_path).st_size
        total_size=total_size+os.stat(name_path).st_size	# CALCULAMOS EL TAMAÑO TOTAL DE TODOS LOS ARCHIVOS
 
 
    for name in dirs:
        name_path=os.path.join(root, name)
        print(name_path) ,
        print os.stat(name_path).st_size
        total_size=total_size+os.stat(name_path).st_size	# CALCULAMOS EL TAMAÑO TOTAL DE TODOS LOS DIRECTORIOS
print "El tamaño total en B es:" , total_size
