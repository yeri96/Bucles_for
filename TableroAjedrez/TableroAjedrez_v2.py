# coding:utf-8

# DEFINIMOS MI RANGO DE NUMEROS (my_range)
def my_range(inici, fi, increment):
	while inici <= fi:
		yield inici
		inici = inici + increment

# HACEMOS LA ESTRUCTURA DE NUESTRO TABLERO (puntos de coordenadas) CON FOR ANIDADOS
for fil in my_range(1, 8, 1):
	for col in my_range(1, 8, 1):
		if ( fil==1 ) or ( fil==7 ):
			if ( col%2==0 ):	# SI EL NUMERO DE COLUMNA ES PAR PARA LAS FILAS 1 Y 7
				print "*",
			else:
				print " ",
		else:
			if ( fil==2 ) or ( fil==8 ):
				if ( col%2==1 ):	# SI EL NUMERO DE COLUMNA ES IMPAR PARA LAS FILAS 2 Y 8
					print "*",
				else:
					print " ",
	print ""	# HACEMOS UN SALTO DE LINEA (intro) CADA VEZ QUE SALGA DEL BUCLE DE COLUMNAS
