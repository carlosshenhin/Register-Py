# configuraciones de logs
import logging
logging.basicConfig(
level=logging.INFO,
format='Fecha:%(asctime)s - User:%(name)s - %(message)s - %(levelname)s',
filename = 'Register_Log.log',
filemode =  'a'
)
# declarar funciones
def F_Buscar():
    print("BUSCAR")

def F_Leer():
    print("LEER")

def F_Escribir():
    print("ESCRIBIR")

def F_Buscar():
    print("BUSCAR")

def F_Borrar():
    print("BORRAR")

def F_Ordenar():
    print("1")
# activar y desactivar log
GV_Log = 3

while GV_Log != 1 and GV_Log != 0 :
        GV_Log = int(input("Activar Log?\n 1 si | 0 no :"))
        if(GV_Log == 1):
            logging.info("log activado")
            print("log activado")
        elif(GV_Log == 0):
            logging.info("log desactivado")
            print("log desactivado")
        else:
            logging.error("valor para 'log switch' invalido")
            print("valor para 'log switch' invalido")
        
# funcionamiento del menu

GV_Seleccion = 1

while GV_Seleccion != 0:
    GV_Seleccion = int(input("Que Operaacion Desea Relizar El Dia De Hoy?\n 1=leer|2=buscar|3=escribir|4=borrar|0=salir :"))
    if(GV_Seleccion == 1):
        F_Leer()
    elif(GV_Seleccion == 2):
        F_Buscar()
    elif(GV_Seleccion == 3):
        F_Escribir()
    elif(GV_Seleccion == 4):
        F_Borrar()
    elif(GV_Seleccion == 0):
        print("Adios")
    else:
        logging.error("caracter invalido invalido")

    

