from bs4 import BeautifulSoup
import requests
import html5lib
import re

req = requests.get('http://clashroyaledeckbuilder.com/cards')

soup = BeautifulSoup(req.text, "html5lib")

def listarcartas():
	puesto = soup.find_all('div', {'class' : 'cardBackground'})
	patron = re.compile('<div class="name"><span>(.*?)</span>')
	nombres= patron.findall(str(puesto))	
	tamanio= len(nombres)
	return nombres

def mostrarcartas():
	listado=listarcartas()
	tamanio= len(listado)
	string=" "
	final= " "
	for x in range(tamanio):
		string = listado[x] +"\n"
		final = final + string
	return final 






