# !/usr/bin/python
# coding:utf-8
import os	# IMPORTAMOS LAS LIBRERIAS
 
path_to_explore="./SHIELD/"

# Mostrem ruta només els arxius
for root, dirs, files in os.walk(path_to_explore):
    for name in files:
            
        name_path=os.path.join(root, name)
        print(name_path)
