# coding: utf-8

#DEFINIMOS MI RANGO DE NUMEROS
def my_range(inici,fi,increment):
	while inici <= fi:
		yield inici
		inici = inici + increment
    
# INICIALIZAMOS EL CONTADOR A 1
contador=1
print "L M M J V S D" # IMPRIMIMOS LA CABECERA

# HACEMOS LA ESTRUCTURA DE NUESTRO CALENDARIO CON FOR ANIDADOS
for fil in my_range(1,6,1):
	for col in my_range(1,7,1):
		if col<=num_dia_mes:
			print contador,
			contador=contador+1
		else:
			print " ",
		for col in my_range(1,dia_semana-1,1):
			print " ",
		for col in my_range(dia_semana,7,1):
			print contador,
			contador=contador+1
	print ""
# FALTA DEFINIR VARIABLES
