# coding: utf-8

def my_range(inici,fi,increment):
	while inici <= fi:
		yield inici
		inici = inici + increment

lista=["L","M","M","J","V","S","D"]		# Definimos la lista
		
lista[2]="X"	#Cambiamos los valores de la lista
lista[0]=0
lista[6]="domingo"

for letras in my_range(0,3,1):
	print lista[letras],		# Imprimimos por pantalla la lista
