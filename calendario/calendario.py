# coding: utf-8

# DEFINIMOS MI RANGO DE NUMEROS (my_range)
def my_range(inici,fi,increment):
	while inici <= fi:
		yield inici
		inici = inici + increment

# INICIALIZAMOS EL CONTADOR A 1
contador=1
print "L M M J V S D"	# IMPRIMIMOS LA CABECERA

# HACEMOS LA ESTRUCTURA DE NUESTRO CALENDARIO CON FOR ANIDADOS
for fil in my_range(1,6,1):
	for col in my_range(1,7,1):
		if fil==1:
			if col==7:
				print contador,
				contador=contador+1	# INCREMENTAMOS EL CONTADOR
			else:
				print " ",
		else:
			if fil>=2:
				if col<=31:
					print contador,
					contador=contador+1
				else:
					print " ",
	print ""	# HACEMOS UN SALTO DE LINEA (intro) CADA VEZ QUE SALGAMOS DEL FOR DE COLUMNAS
