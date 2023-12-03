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
print(f"\nPerfecto {nombre}, empezando el juego de ahorcado: \n")

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

#Esta funcion con la ayuda de la libreria random, y el randint toma un valor entre 0 y la longitud
# de la lista diccionario -1 para despues regresar la palabra sacandola por el valor obtenido de la lista
def Palabra_al_Azar(diccionario):
    palabraOculta = rdn.randint(0, len(diccionario) - 1)
    return diccionario[palabraOculta]
#Aqui somplemente la funcion actualiza que numero en la lista de dibujos va a llmar depende
# de cuantos erorres lleve el usuario, al inicio lleva 0 por lo que imprime el primer elemento
def Diseño_ahorcado():
    print(dibujos[len(letras_incorrectas)],"\n")

#-------------------------------------------------------------------------

#1: llama a la funcion previa para que saber si aun tienes intentos, imprimir la lista casillas y
# las letras incorrectas que llevas, con el asterisco se desglosan los elementos de la lista, asi mostrandolos
def Tablero():
    Diseño_ahorcado()
    if len(letras_incorrectas) < 6:
        print(*casillas)
        print("\n Letras incorrectas que llevas: ", *letras_incorrectas)
def Letra_Valida():
    if letra in "abcdefghijklmnñopqrstuvxyzw" and len(letra) == 1:
        return True
    elif len(letra) > 1:
        print("\n \n \n \n ingresa solo una letra a la vez")
        return False
    elif letra not in "abcdefghijklmnñopqrstuvxyzw":
        print("\n \n \n \n Solamente se aceptan letras del abedecario, Prueba otra vez")
        return False
#3: Esta funcion es para ver si la letra ingrsada ya fue ingresada previamente
def Letra_Repetida():
    if letra in letras_incorrectas:
        print("\n \n \n Ya te equivocaste con esa letra")
        return True
    elif letra in casillas:
        print("\n \n \n Ya atinaste esa letra")   
        return True
    else:
        return False