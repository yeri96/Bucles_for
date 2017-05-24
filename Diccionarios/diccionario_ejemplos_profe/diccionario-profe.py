 
# coding:utf-8
 
####################################################
def my_range(inici, fi, increment):
    while inici <= fi:
        #Retorna l'element actual del rang (llista)
        yield inici
        inici = inici + increment
####################################################
#Crear diccionario
 
diccionario={"Piloto 1":"Fernando Alonso",
             "Piloto 2":"Kimi Raikkonen",
             "Piloto 3":"Felipe Massa"}
print diccionario
 
# Obtener valor
print diccionario["Piloto 2"]
print diccionario.get("Piloto 2")
print diccionario
 
# Obtener valor y sacarla del diccionario
print diccionario.pop("Piloto 2")
print diccionario
 
# Vuelvo a generar el diccionario original
diccionario={"Piloto 1":"Fernando Alonso",
             "Piloto 2":"Kimi Raikkonen",
             "Piloto 3":"Felipe Massa"}
print diccionario
print len(diccionario)
 
 
#Modificar valor existente
diccionario["Piloto 3"]="Fast Ivan & very furious"
print diccionario
 
#Añadir nuevo (clave+valor)
diccionario["Piloto 4"]="Zeus"
print diccionario
