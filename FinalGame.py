#Creamos el juego donde el jugador debe intoducir un número aleatorio entre 0 y 100, debiendo adivinar dicho número.
#Metodo para generar el número aleatorio dentro del rango.
import random
#Creamos una función para seleccionar el nivel en el que se quiera jugar una vez iniciado el juego

def choose_level():
    print ("-->Seleccione el nivel de dificultad deseado entre las siguientes opciones:")
    print("Nivel 1: Simple\n")
    print("Nivel 2: Intermedio\n")
    print("Nivel 3: Avanzado\n")
    print("Nivel 4: Experto\n")
    level_chossen = int(input("-->Seleccione el nivel deseado de juego (1-4):"))
    global level_option 
    level_option = level_chossen
    if 0 < level_chossen <= 4 :
        if level_chossen == 1:
            print("Ha seleccionado el nivel de dificultad simple.")
        if level_chossen == 2:
            print("Ha seleccionado el nivel de dificultad intermedio.")
        if level_chossen == 3:
            print("Ha seleccionado el novel de dificultad avanzado.")
        if level_chossen == 4:
            print("Ha seleccionado el nivel de dificultad experto.")
    else:
        print("\n-->Por favor, selccione uno de los cuatro niveles de dificultad disponibles.")

#Empezamos a diseñar el juego con una funcion definida dependiendo del nivel de dificultad elegido
#Fijamos las condiciones
def game():
    print("-->Eliga un modo de juego (1-2):")
    print("\n1 = Propio Usuario")
    print("\n2 = IA")
    chossen_level = int(input("-->Seleccione el modo deseado de juego (1-2):"))
    chossen_mode = chossen_level
    if 0 < chossen_mode <= 4 :
        if chossen_mode ==1 :
            print("El modo seleccionado fue Propio Usuario.")
        if chossen_mode == 2 :
            print("El modo seleccionado fue IA.")
    else:
        print("\n-->Por favor, seleccione uno de los dos modos disponibles.")
        
    if chossen_mode == 1:
        times = 0
        while times < maxtime:
            print("\n-->Intente adivinar el número:")
            time = int(input())
            times += 1
            
            
            if time < number:
                print("-->Su número es menor que el generado aleatoriamente.\n")
            if time > number:
                print("--> Su número es mayor que el generado aleatoriamente\n")
            if time == number:
                break
        if time == number:
            print("\n¡Enhorabuena! Has adivinado el número aleatorio en" ,str(times), "oportunidades.")
            score = maxtime - times
        if time != number:
            print("Otra vez será, no ha logrado adivinar el número aleatorio en los" + str(maxtime) + "intentos posibles.")
        
        
    if chossen_mode == 2:
        times = 0
        minIA = min
        maxIA = max 
        time = (minIA + maxIA)//2
        while time != number and times < maxtime: 
            time = (minIA + maxIA)//2
            times += 1
            print("La IA ha comprobado el número introducido" + str(time) + "y")
            if time > number:
                print("este se encuentra por encima del número proporcionado.\n")
                maxIA = time
            elif time < number:
                print("este se encuentra por debajo del número proporcionado.\n")
                minIA = time + 1
        print("es el número a adivinar.\n")
        print("Ha tardado" + str(times) + ("intentos."))

choose_level()


if level_option == 1:
    maxtime = 15
    times = 0
    min = 0
    max = 100
    number = random.randint(min, max)
    print("\nPor favor, inserte el número a adivina generado aleatoriamente entre el 0 y el 100.")
    game()
    
if level_option == 2:
    maxtime = 45
    times = 0
    min = 0
    max = 1000
    number = random.randint(min, max)
    print("\nPor favor, inserte el número a adivina generado aleatoriamente entre el 0 y el 1000.")
    game()
    
if level_option == 3:
    maxtime = 75
    times = 0
    min = 0
    max = 10000
    number = random.randint(min, max)
    print("\nPor favor, inserte el número a adivina generado aleatoriamente entre el 0 y el 10000.")
    game()
    
if level_option == 4:
    maxtime = 105
    times = 0
    min = 0
    max = 100000
    number = random.randint(min, max)
    print("\nPor favor, inserte el número a adivina generado aleatoriamente entre el 0 y el 100000.")
    game()