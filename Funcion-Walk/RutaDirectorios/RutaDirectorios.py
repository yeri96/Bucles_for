# !/usr/bin/python    # CON ESTA LINEA LE DECIMOS QUE LO QUE VIENE A CONTINUACION ES UN SCRIPT EN PYTHON
# coding:utf-8
import os	# IMPORTAMOS LAS LIBRERIAS
 
path_to_explore="./SHIELD/"

# MOSTRAMOS LA RUTA SOLO DE LOS DIRECTORIOS
for root, dirs, files in os.walk(path_to_explore):
    for name in dirs:
            
        name_path=os.path.join(root, name)
        print(name_path)
