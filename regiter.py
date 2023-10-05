# declarar funciones

# activar y desactivar log
log = int(input("Activar Log?\n 1 si | 0 no :"))

# funcionamiento del menu
seleccion = 1

while seleccion != 0:
    seleccion = int(input("Que Operaacion Desea Relizar El Dia De Hoy?\n 1=leer|2=buscar|3=escribir|4=borrar|0=salir :"))
    if(seleccion == 1):
        print("ejemplo de funcionamiento 1")
    elif(seleccion == 2):
        print("ejemplo de funcionamiento 2")
    elif(seleccion == 3):
        print("ejemplo de funcionamiento 3")
    elif(seleccion == 4):
        print("ejemplo de funcionamiento 4")
    elif(seleccion == 0):
        print("Adios")
    else:
        print("valor invalido")

    

