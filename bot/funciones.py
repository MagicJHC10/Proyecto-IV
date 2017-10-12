#LISTA CON PERSONAJE Y PUNTOS DE VIDA
lista = {"Principe":1463,"Princesa":216,"Golem":4256}

def extraerPuntosVida(name):
	return lista.get(name)


print extraerPuntosVida("Principe")

#Ordena los personajes por puntos de vida
def clasificacionPersonajesVida():
	listado= sorted(lista.items(),key= lambda lista: lista[1])
	cadena = " "
	for x in listado:
		cadena = " Personaje " + x[0] + " Puntos de vida " + str(x[1])+ "\n" + cadena 

	return cadena

print clasificacionPersonajesVida()
