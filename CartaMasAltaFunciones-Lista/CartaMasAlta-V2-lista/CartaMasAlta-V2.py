# coding:utf-8
# Les cartes son: 1-10,J,Q,K (total 13)


######################################################
# Definimos my_range
def my_range(inici, fi, increment):
    while inici <= fi:
        #Retorna l'element actual del rang (llista)
        yield inici
        inici = inici + increment
######################################################

# Importamos randint
from random import randint

# Generamos un numero aleatorio entre 0 y 12 (coge un numero aleatorio que representará la posicion de la lista)
j1num=randint(0,12)

cartas=[1,2,3,4,5,6,7,8,9,10,"J","Q","K"]	# creamos la listas con las cartas a mostrar

numero=j1num	# guardamos el numero aleatorio en esta variable al vuelo
for jugada1 in my_range(1,1,1):
	print "Jugador1 juega con :", cartas[numero]

# Generamos un numero aleatorio entre 0 y 12 (coge un numero aleatorio que representará la posicion de la lista)
j2num=randint(0,12)

numero=j2num	# guardamos el numero aleatorio en esta variable al vuelo
for jugada2 in my_range(1,1,1):
	print "Jugador2 juega con :", cartas[numero]


# Comprovem si hi ha empat
if (j1num==j2num):
    print "Empate"
else:
    if (j1num>j2num):
        print "Gana jugador1"
    else:
        print "Gana jugador2"
