# coding: utf-8

def my_range(inici,fi,increment):   # definimos my_range
	while inici <= fi:
		yield inici
		inici = inici + increment

lista=["Hola"]		# Definimos la lista

	# Añadimos la palabra mundo en el último valor de la lista
lista.append("mundo")
lista.append("!")

for saludo in my_range(0,2,1):
	print lista[saludo], 	# Imprimimos por pantalla la lista
