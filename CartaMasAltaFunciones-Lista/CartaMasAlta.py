# coding: utf-8

############################################################################
#                              QUE HACE?
# Posibilidades: Elegir una carta 1-13
# Jugador1 machine
# Jugador2 machine
# Gana la carta más alta
# 
############################################################################


############################################################################
#                               IMPORT
############################################################################
from random import randint	


############################################################################
#                        VARIABLES GLOBALES
############################################################################
aleatori1=randint(1,13)	# Generamos numeros aleatorios entre 1-13
aleatori2=randint(1,13)
lista=["J","Q","K"]		# Creamos la lista para los numeros 11,12, y 13

############################################################################
#                               NIVEL 4
############################################################################
def jugador1():			# Para el jugador1
	if aleatori1>10 :	# Cuando sea mayor de 10 nos mostrará la letra correspondiente
		if aleatori1==11:
			for figura in lista[0]:	# Cogemos la posicion 0 de la lista y metemos su valor en la variable figura
				print "máquina1 juega con : ", figura	# Imprimimos por pantalla el valor de la variable (J)

		if aleatori1==12:
			for figura in lista[1]:
				print "máquina1 juega con : ", figura
		
		if aleatori1==13:
			for figura in lista[2]:
				print "máquina1 juega con : ", figura

	else:
		print "máquina1 juega con : ", aleatori1	# Imprimimos por pantalla el número generado por el jugador1

############################################################################
#                               NIVEL 3
############################################################################
def jugador2():
	if aleatori2>10 :
		if aleatori2==11:
			for figura in lista[0]:
				print "máquina2 juega con : ", figura

		if aleatori2==12:
			for figura in lista[1]:
				print "máquina2 juega con : ", figura
	
		if aleatori2==13:
			for figura in lista[2]:
				print "máquina2 juega con : ", figura

	else:
		print "máquina2 juega con : ", aleatori2	# Imprimimos por pantalla el número generado por el jugador2


############################################################################
#                               NIVEL 2
############################################################################
def ganador_empate():
	if aleatori1==aleatori2 :
			print "Empate"
	else:
		if aleatori1>aleatori2 :
			print "Gana máquina1"
		else:
			print "Gana máquina2"
	
############################################################################
#                               NIVEL 1
############################################################################

# Llamamos a todas las funciones definidas para que sean ejecutadas
jugador1()
jugador2()
ganador_empate()
