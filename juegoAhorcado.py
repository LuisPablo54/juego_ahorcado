#Proyecto Final - Programación

#Integrantes:

#Rodrigo Mendoza Rodriguez
#Luis Pablo López Iracheta


#Aqui importamos la libreria random para una funcion de alatoriedad que usaremos adelante
import random as rdn


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
        with open("C:/Users/Personal Computer/OneDrive/Documentos/BancoDePalabrasDificil.txt","r") as archivo:
            lineas = archivo.readlines()
            palabras = [palabra.strip() for linea in lineas for palabra in linea.split()]
            palabraAleatoria = rdn.choice(palabras).strip()

    elif dificultad == "intermedio":
        print("\nBuena opcion, siempre en equilibrio \n")
        with open("C:/Users/Personal Computer/OneDrive/Documentos/BancoDePalabrasIntermedio.txt","r") as archivo:
            lineas = archivo.readlines()
            palabras = [palabra.strip() for linea in lineas for palabra in linea.split()]
            palabraAleatoria = rdn.choice(palabras).strip()
         
    elif dificultad == "facil":
        print("\nVienes a relajarte, perfercto \n")
        with open("C:/Users/Personal Computer/OneDrive/Documentos/BancoDePalabrasFacil.txt","r") as archivo:
            lineas = archivo.readlines()
            palabras = [palabra.strip() for linea in lineas for palabra in linea.split()]
            palabraAleatoria = rdn.choice(palabras).strip()
    #Si el usuario elige una categoria inexistente que "nuevojuego" valga otra vez true y con el "continue" se vuelva a ejecutar desde el primer bucle
    else:
        print("\n La opcion seleccionada no esta disponible, de favor corrige tu escritura \n")
        nuevojuego = True
        continue

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
        print("\n \n \n \n Solamente se aceptan letras del abedecario")
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
        if letra in palabraAleatoria:
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
    for i in range(len(palabraAleatoria)):
        if palabraAleatoria[i] == letra:
            casillas[i] = letra
#Comprueba si ya no quedan guiones bajos en la lista casillas porque ya todos fueron cambiados por letras
def Victoria():
    if " _" not in casillas:
        print("Felicidades ", nombre,"!!! Descubriste la palabra por completo, que listo que sos")
        print("La palabra era", palabraAleatoria)
        return True
#Si la lista de letras incorrectas alcanza 6 elementos en ella, quiere decir que perdiste
def Perder():
    if len(letrasIncorrectas) == 6:
        print("F en el chat ¡Lo siento", nombre,"! ¡Has perdido! la palabra a adivinar era: " ,palabraAleatoria)
        return True
#Ingresamos esta funcion para usarla en el bucle del juego para que, cuando pierdas no se cierre tan abruptamente el programa.
def TableroFinal():
    DiseñoAhorcado()
    if len(letrasIncorrectas) < 6:
        print(*casillas)

#-------------------------------------------------------------------------

#La lista casillas van a ser tantos guiones como la cantidad de letras de la palabra
casillas = [ " _" ]*len(palabraAleatoria)
letrasIncorrectas = []

confirmacion = True
while confirmacion == True:
    
    #Llamamos la funcion #1, para que imprima el dibujo del ahorcado con indice 0 (el primero seria)
    Tablero()
    #Le pedimos al usuario que iongrese una letra, la pasamos a minusculas y le quitamos los espacios.
    letra = input("\nAhora ¿Con cual letra quiere probar su suerte?  ")
    letra = letra.lower()
    letra = letra.strip()
    print("-------------------------------------------------------------------------------------------------------")
    #Ahora si con la funcion #2 vemos si el usuario solo ingreso una letra y no simbolos, dos letras, etc.
    #Pero tambien vemos si la letra no esta repetida, cuando se cumplen las dos condiciones se ejecuta el bloque
    if LetraValida() == True and LetraRepetida() == False:
        Comprobar()
        ActualizarCasillas()
        if Victoria() == True:
            TableroFinal()
            input(":D\n \nPresiona enter para terminar. ")
            confirmacion = False
        if Perder() == True:
            Tablero()
            input("D:\n \nPresiona enter para terminar. ")
            confirmacion = False
                
    #Si en el "if" no se fue por ninguna quiere decir que sigue jugando asi que, le ponemos que lo intente otra vez
    # y con el "continue" el bloque principal se volveria a ejecutar, pidiendo una letra, comprobando, etc.
    else:
        print("intentalo de nuevo ", nombre)
        confirmacion = True
        continue
    
#---------------------------------------------------------------------------