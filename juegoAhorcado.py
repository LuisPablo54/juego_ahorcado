#Proyecto Final - Programación

#Integrantes:

#Rodrigo Mendoza Rodriguez
#Luis Pablo López Iracheta


#Aqui importamos la libreria random para una funcion de alatoriedad que usaremos adelante
import random as rdn


#Banco de palabras

Facil = ["amarillo","verde","rojo","violeta","turquesa","marron","naranja","aguamarina","dorado","blanco"]

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

#Primero vamos a elegir con que palabara vamos a trabajar, para eso nos basamos en las preferencias del usuario
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
def PalabraAlAzar(diccionario):
    palabraOculta = rdn.randint(0, len(diccionario) - 1)
    return diccionario[palabraOculta]
#La funcion actualiza que numero en la lista de dibujos va a llamar depende de cuantos erorres lleve el usuario
def DiseñoAhorcado():
    print(dibujos[len(letrasIncorrectas)],"\n")

#-------------------------------------------------------------------------

#Llama a la funcion previa para que saber si aun tienes intentos, imprime la lista casillas y
# las letras incorrectas que llevas, con el asterisco se desglosan los elementos de la lista, asi mostrandolos
def Tablero():
    DiseñoAhorcado()
    if len(letrasIncorrectas) < 6:
        print(*casillas)
        print("\n Letras incorrectas que llevas: ", *letrasIncorrectas)
def LetraValida():
    if letra in "abcdefghijklmnñopqrstuvxyzw" and len(letra) == 1:
        return True
    elif len(letra) > 1:
        print("\n \n \n \n ingresa solo una letra a la vez")
        return False
    elif letra not in "abcdefghijklmnñopqrstuvxyzw":
        print("\n \n \n \n Solamente se aceptan letras del abedecario, Prueba otra vez")
        return False
#Esta funcion es para ver si la letra ingrsada ya fue ingresada previamente
def LetraRepetida():
    if letra in letrasIncorrectas:
        print("\n \n \n Ya te equivocaste con esa letra")
        return True
    elif letra in casillas:
        print("\n \n \n Ya atinaste esa letra")   
        return True
    else:
        return False
#Checa si descubirste una letra, y si no que la anexe a la lista de letras incorrectas,
#pero si era la ultima letra por descubir y la acertaste, imprime que fue la ultima.
def Comprobar():
    if len(letrasIncorrectas) < 6:
        if letra in palabra:
            print("\n \n \n \n Perfecto le atinaste a una!\n")
        elif Victoria() == True:
            print("\n \n \n \n Perfecto, le atinaste a la ultima")
        else:
            print("\n \n \n \n Esa letra no era, intentalo de nuevo :(\n")
            letrasIncorrectas.append(letra)
#Comprobamos si la letra esta en la palabra para sutituirla por el guion =>
# si el elemento de la lista de la palabra con indice "i" es igual a la letra del usuario, 
# entonces en la lista "casillas" va a ser remplazado por la letra del usuario.
def ActualizarCasillas():
    for i in range(len(palabra)):
        if palabra[i] == letra:
            casillas[i] = letra
#Comprueba si ya no quedan guiones bajos en la lista casillas porque ya todos fueron cambiados por letras
def Victoria():
    if " _" not in casillas:
        print("Felicidades ", nombre,"!!! Descubriste la palabra por completo, que listo que sos")
        print("La palabra era", palabra)
        return True
#Si la lista de letras incorrectas alcanza 6 elementos en ella, quiere decir que perdiste
def Perder():
    if len(letrasIncorrectas) == 6:
        print("F en el chat ¡Lo siento", nombre,"! ¡Has perdido! la palabra a adivinar era: " ,palabra)
        return True
#Ingresamos esta funcion para usarla en el bucle del juego para que, cuando pierdas no se cierre tan abruptamente el programa.
def TableroFinal():
    DiseñoAhorcado()
    if len(letrasIncorrectas) < 6:
        print(*casillas)