#Proyecto Final - Programación

#Integrantes:

#Rodrigo Mendoza Rodriguez
#Luis Pablo López Iracheta


#Aqui importamos la libreria random para una funcion de alatoriedad que usaremos adelante
import random as rdn


#Banco de palabras

Facil = ["amarillo","verde","rojo","violeta","turquesa","marron","naranja","aguamarina","dorado","blanco",]

Intermedio = ["turquia","suecia","argentina","ucrania","brasil","canada","dinamarca","francia","polonia"]

Dificil = ["hortensia","azalea","pensamiento","orquidea","margarita","hibisco","bugambilia","lavanda","dalia","azucena"]



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

#Menu de niveles par el usuario

nombre = str(input("Nombre del jugador: "))
print(f"\nPerfecto {nombre}, empezando el juego de arcado: \n")

#Primero vamos a elegir con que plabara vamos a trabajar, para eso nos basamos en las preferencias del usuario
#Lo de nuevo juego true y flase, solo es para lograr hacer un bucle, por si el usuario
#no elige una opcion existente le vuelva a preguntar hasta que eliga una que si existe
nuevojuego = True
while nuevojuego == True:
    nuevojuego = False
    print("Primero, ¿Que dificultad deseas?")
    print("\n Dificil \n Intermedio \n Facil \n")
    dificultad = input()
    #.Lower => es para pasar todas las letras de la variable a minusculas
    dificultad = dificultad.lower()
    #.strip => Elimina todos los espacios antes o despues en la cadena de texto
    dificultad = dificultad.strip()
    #aqui ya inician las deciciones, depende de la dificultat que desee el usuario
    if dificultad == "dificil":
        print("\nBuscas reto?, p\n")    
        diccionario = Intermedio

    elif dificultad == "intermedio":
        print("\nBuena opcion, siempre en equilibrio \n")
        diccionario = Intermedio
         
    elif dificultad == "facil":
        print("\nVienes a relajarte, perfercto \n")
        diccionario = Facil
    #Si el usuario elige una categoria inexistente que "nuevojuego" valga otra vez true y con el "continue" se vuelva a ejecutar desde el primer bucle
    else:
        print("\n La opcion seleccionada no esta disponible, de favor corrige tu escritura \n")
        nuevojuego = True
        continue

