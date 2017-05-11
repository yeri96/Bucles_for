# coding:utf-8

# DEFINIMOS NUESTRO RANGO DE NUMEROS
def my_range(inici, fi, increment):
	while inici <= fi:
		yield inici
		inici = inici + increment

# HACEMOS LA ESTRUCTURA DE NUESTRO TABLERO (puntos de coordenadas) CON FOR ANIDADOS
for fil in my_range(1, 4, 1):
	for col in my_range(1, 8, 1):
		if (( fil==1 ) or ( fil==4 )):
			print "*",
		else:
			if (( col==1 ) or ( col==8 )):
				print "*",
			else:
				if ( fil==2):
					if ( col==4 ):
						print "·",
					elif ( col==5 ):
						print "·",
					else:
						print " ",
				else:
					if ( fil==3 ):
						if ( col==4 ):
							print "|",	# AQUI CAMBIAMOS \ POR | PORQUE CONTRABARRA ES UN CARACTER ESPECIAL
						elif ( col==5 ):
							print "|",
						else:
							print " ",
	print ""	# HACEMOS UN SALTO DE LINEA (intro) CADA QUE SALCA DEL BUCLE DE COLUMNAS
