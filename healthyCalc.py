def menu():
    print("\n*****  Calculadora Saludable  *****\n")
    print("1. Peso ideal\n2. Calorías quemadas\n3. Porcentaje grasa corporal\n4. Índice metabólico basal")

def calculadora():
    try:
        userOpt = int(input("\nIngrese un número de las opciones del menú: "))
    except:
        print("Opción no válida; intente nuevamente")
        exit()
    if userOpt == 1:
        try:
            userTall = int(input("Ingrese su altura en cm: "))
            gender = input("Ingrese m para género masculino ó f para género femenino: ").lower()
            if gender == "m":
                ibwm = round(56.2 + 1.41*((userTall/2.54)-60),2)
                print("Su peso ideal es:",ibwm)
            elif gender == "f":
                ibwf = round(53.1 + 1.36*((userTall/2.54)-60),2)
                print("Su peso ideal es:",ibwf)
            else:
                print("Opción no válida")
        except:
            print("Datos inválidos; intente nuevamente")
            exit()
    if userOpt == 2:
        print("\nOpciones de actividades:\n1. Caminar\n2. Tenis\n3. Montar en bicicleta\n4. Correr\n5. Nadar\n")
        try:
            userAct = int(input("Ingrese el número correspondiente a la actividad que usted realiza: "))
            if userAct < 1 or userAct > 5:
                print("Opción no válida")
                exit()
            elif userAct == 1:
                met = 2
            elif userAct == 2:
                met = 5
            elif userAct == 3:
                met = 14
            elif userAct == 4:
                met = 6
            elif userAct == 5:
                met = 9.8
            actTime = int(input("Cuánto tiempo en minutos realiza de la actividad: "))
            userWeight = float(input("Ingrese su peso en kg: "))
            burnedCal = actTime*met*(userWeight/200)
            print("Calorías quemadas:",burnedCal)
        except:
            print("Datos inválidos; intente nuevamente")
            exit()
    if userOpt == 3:
        try:
            userWeight = float(input("Ingrese su peso en kg: "))
            userTall = float(input("Ingrese su altura en m: "))
            imc = (userWeight/userTall)
            userAge = int(input("Ingrese su edad en años: "))
            gender = input("Ingrese m para género masculino ó f para género femenino: ").lower()
            if gender == "m":
                pgcm = round((1.20 * imc) + (0.23 * userAge) - 16.2, 2)
                print("El porcentaje de grasa corporal es:",pgcm,"%")
            elif gender == "f":
                pgcf = round((1.20 * imc) + (0.23 * userAge) - 5.4, 2)
                print("El porcentaje de grasa corporal es:",pgcf,"%")
            else:
                print("Opción no válida")
        except:
            print("Datos inválidos; intente nuevamente")
            exit()
    if userOpt == 4:
        try:
            userWeight = float(input("Ingrese su peso en kg: "))
            userTall = int(input("Ingrese su altura en cm: "))
            userAge = int(input("Ingrese su edad en años: "))
            gender = input("Ingrese m para género masculino ó f para género femenino: ")
            if gender == "m":
                imbm = round(13.397*userWeight + 4.799*userAge + 5.677*userTall + 88.362, 2)
                print("El índice metabólico basal es de:",imbm)
            elif gender == "f":
                imbf = round(9.247*userWeight + 3.098*userAge + 4.330*userTall + 447.593, 2)
                print("El índice metabólico basal es de:",imbf)
            else:
                print("Opción no válida")
        except:
            print("Datos inválidos; intente nuevamente")
            exit()

menu()
calculadora()


