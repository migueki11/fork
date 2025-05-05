import os


os.system('cls')

def jugador_de_padel():
    # Declaración de variables
    nombre = ""
    edad = 0
    energia = 100
    habilidades = 50
    titulos = 0
    dinero = 1000
    decision = ""
    carrera_activa = True
    contrato_profesional = False
    colaboracion = False
    
    # Inicialización del jugador
    os.system('cls')
    print("¡Bienvenido al simulador de tu carrera de jugador de pádel!")
    nombre = input("Por favor, introduce tu nombre: ")
    edad = int(input("Por favor, introduce tu edad: "))
    
    # Bucle principal
    while carrera_activa:
        # Mostrar estado del jugador
        os.system('cls')
        print("\nJugador:", nombre)
        print("Edad:", edad, "años")
        print("Energía:", energia, "%")
        print("Habilidades:", habilidades, "%")
        print("Títulos ganados:", titulos)
        print("Dinero: $", dinero)
        
        if contrato_profesional:
            print("Tienes un contrato profesional.")
        else:
            print("No tienes contrato profesional aún.")
        
        if colaboracion:
            print("Estás en colaboración con otro jugador.")
        else:
            print("No estás colaborando con nadie en este momento.")
        
        print("")
        
        # Opciones principales
        print("¿Qué deseas hacer a continuación?")
        print("1) Entrenar en el club local (-20 energía, +10 habilidades, -$100)")
        print("2) Participar en un torneo local (-30 energía, +1 título si ganas, +$500 si tienes contrato)")
        print("3) Participar en un torneo internacional (-50 energía, +3 títulos si ganas, +$1000 si tienes contrato)")
        print("4) Descansar en casa (+30 energía)")
        print("5) Buscar un patrocinador (si tienes al menos 70 habilidades y 2 títulos)")
        print("6) Colaborar con otro jugador (mejora habilidades pero consume dinero)")
        print("7) Retirarte de la carrera")
        
        decision = input("Elige una opción (1-7): ")
        
        # Evaluar decisión del jugador
        if decision == "1":
            if energia >= 20:
                if dinero >= 100:
                    energia -= 20
                    habilidades += 10
                    dinero -= 100
                    print("Entrenaste en el club y tus habilidades mejoraron.")
                else:
                    print("No tienes suficiente dinero para entrenar.")
            else:
                print("No tienes suficiente energía para entrenar.")
        
        elif decision == "2":
            if energia >= 30:
                energia -= 30
                if habilidades >= 70:
                    titulos += 1
                    print(f"¡Ganaste el torneo local! Ahora tienes {titulos} títulos.")
                   
                    if contrato_profesional:
                        dinero += 500
                        print("Tu contrato te dio $500 por este torneo.")
                else:
                    print("Perdiste el torneo local. Necesitas entrenar más.")
            else:
                print("No tienes suficiente energía para participar en un torneo local.")
        
        elif decision == "3":
            if energia >= 50:
                energia -= 50
                if habilidades >= 80:
                    titulos += 3
                    print(f"¡Ganaste el torneo internacional! Ahora tienes {titulos} títulos.")
                    if contrato_profesional:
                        dinero += 1000
                        print("Tu contrato te dio $1000 por este torneo.")
                else:
                    print("Perdiste el torneo internacional. Necesitas entrenar más.")
            else:
                print("No tienes suficiente energía para participar en un torneo internacional.")
        
        elif decision == "4":
            energia += 30
            if energia > 100:
                energia = 100
            print("Descansaste y recuperaste energía.")
        
        elif decision == "5":
            if habilidades >= 70:
                if titulos >= 2:
                    contrato_profesional = True
                    dinero += 1000
                    print("¡Felicidades! Has conseguido un patrocinador y un contrato profesional.")
                    print("Has recibido $1000 como adelanto.")
                else:
                    print("No tienes suficientes títulos para obtener un patrocinador.")
            else:
                print("No tienes suficientes habilidades para obtener un patrocinador.")
        
        elif decision == "6":
            if dinero >= 500:
                colaboracion = True
                dinero -= 500
                habilidades += 15
                print("Iniciaste una colaboración con otro jugador. Tus habilidades mejoran.")
            else:
                print("No tienes suficiente dinero para colaborar.")
        
        elif decision == "7":
            print("Te has retirado de la carrera. ¡Gracias por jugar!")
            carrera_activa = False
        
        else:
            print("Opción no válida. Intenta de nuevo.")
        
        # Limpiar la pantalla después de elegir una opción
        os.system('cls')
        
        # Incremento de edad
        edad += 1
        
        # Verificar fin de la carrera
        if edad >= 35:
            print(f"\nTu carrera ha llegado a su fin a los {edad} años.")
            print(f"Títulos finales ganados: {titulos}")
            print(f"Dinero acumulado: ${dinero}")
            carrera_activa = False
        
        # Esperar a que el jugador presione una tecla para continuar
        input("\nPresiona Enter para continuar...")

# Llamar a la función principal para iniciar el simulador
jugador_de_padel()