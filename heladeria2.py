opcion = ""
cestrellan = 0
champs = 0
meganium = 0
donkie = 0
totalVentas = 0

print("=== Bienvenido a Heladeria Fan's Levi Live ===")
print("Los helado disponibles son:")
print("Cestrellan (500 pesos), Champs (4.000 pesos), meganium (2.500 pesos), Donkie (2.000 pesos)")
while opcion != "5":
    print("1- Cestrellan")
    print("2- Champs")
    print("3- Meganium")
    print("4- Donkie")
    print("5- Salir")

    opcion = input("Ingrese una opción:")

    if opcion not in ("1", "2", "3", "4", "5"):
        print("La opción no es válida")
    elif opcion == "1":
        print("Usted quiere un Cestrellan")
        print("Gracias por su compra")
        cestrellan+= 1
        totalVentas += 500
        edad = int(input("ingrese su edad: "))
        if edad > 18 or edad < 65:
            if edad < 18 or edad > 65:
                print("Tiene un descuento del 10%")
                totalVentas -= (500 * 10 / 100)
    elif opcion == "2":
        print("Usted quiere un Champs")
        print("Gracias por su compra")
        champs+= 1
        totalVentas+=4000
        edad = int(input("ingrese su edad: "))
        if edad > 18 or edad < 65:
            if edad < 18 or edad > 65:
                print("Tiene un descuento del 10%")
                totalVentas -= (4000 * 10 / 100)
    elif opcion == "3":
        print("Usted quiere un Meganium")
        print("Gracias por su compra")
        meganium+= 1
        totalVentas+=2500
        edad = int(input("ingrese su edad: "))
        if edad > 18 or edad < 65:
            if edad < 18 or edad > 65:
                print("Tiene un descuento del 10%")
                totalVentas -= (2500 * 10 / 100)
    elif opcion == "4":
        print("Usted quiere un donkie")
        print("Gracias por su compra")
        donkie+= 1
        totalVentas+=2000
        edad = int(input("ingrese su edad: "))
        if edad > 18 or edad < 65:
            
            if edad < 18 or edad > 65:
                print("Tiene un descuento del 10%")
                totalVentas -= (2000 * 10 / 100)
    else:
        print("=== Reporte total de ventas ===")
        print("Cestrellan: ", cestrellan)
        print("Champs: ", champs)
        print("Meganium: ", meganium)
        print("Donkie: ", donkie)
        print("Total ventas: ", totalVentas)
        print("=== Fin del reporte ===")