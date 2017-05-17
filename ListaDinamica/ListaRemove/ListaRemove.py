# coding: utf-8

def my_range(inici,fi,increment):	# Definimos my_range
	while inici <= fi:
		yield inici
		inici = inici + increment

lista=["Es","un","mal","día"]		# Definimos la lista

lista.remove("mal")		# Eliminamos el valor de la posición 2 (mal) de la lista
lista.insert(2,"buen")		# Añadimos el valor (buen) en la posición 2 de la lista

for frase in my_range(0,3,1):
	print lista[frase], 	# Imprimimos por pantalla la lista
