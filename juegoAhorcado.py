#Proyecto Final - Programación

#Integrantes:

#Rodrigo Mendoza Rodriguez
#Luis Pablo López Iracheta


#Aqui importamos la libreria random para una funcion de alatoriedad que usaremos adelante
import random as rdn


#Banco de palabras: son las listas que contienen las posibles palabras a a elegir
AnimalesFacil = ["perro","vaca","delfin","caballo","gato","leon","panda","jirafa","pez","jaguar"]

ColoresFacil = ["amarillo","verde","rojo","violeta","turquesa","marron","naranja","aguamarina","dorado","blanco",]

DeportesFacil = ["atletismo","esgrima","ciclismo","golf","natacion","tenis","baloncesto","boxeo","futbol","hockey"]

PaisesIntermedio = ["turquia","qatar","suecia","argentina","ucrania","brasil","canada","dinamarca","francia","polonia"]

ComidasIntermedio = ["guacamaya","torta","mole","pozole","palomitas","crepas","paella","poutine","tacos","tofu","pescado"]

MarcasIntermedio = ["adidas","honda","sony","whatsapp","canon","pinterest","facebook","airbnb","starbucks","youtube"]

FlorDificil = ["hortensia","azalea","pensamiento","orquidea","margarita","hibisco","bugambilia","lavanda","dalia","azucena"]

CiudadesDificil = ["villahermosa","aguascalientes","poroy","batman","bankok","xbox","copenhague","melbourne","amsterdam"]

InglesDificil = ["chemical","bought","nonplussed","whom","account","conversation","friend","group","indeed","international"]

#Dibujo del ahorcado: una lista con 7 elementos que basicamente son dibujos echos con simbolos
dibujos = ['''
     +----¬
     |    |
     |      
     |      
     |      
     |     
    =========
    /       \ ''', '''
     +----¬
     |    |
     |    O
     |     
     |     
     |     
    =========
    /       \ ''', '''
     +----¬
     |    |
     |    O 
     |    | 
     |     
     |
    =========
    /       \ ''', '''
     +----¬
     |    |
     |    O 
     |   /| 
     |     
     |     
    =========
    /       \ ''', '''
     +----¬
     |    |
     |    O 
     |   /|\ 
     |     
     |  
    =========
    /       \ ''', '''
     +----¬
     |    |
     |    O 
     |   /|\ 
     |   / 
     |
    =========
    /       \ ''', '''
     +----¬
     |    |
     |    0 
     |   /|\ 
     |   / \ 
     |
    =========
    /       \ ''']