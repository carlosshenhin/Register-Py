# variables globales
GV_Log = 3
GV_Seleccion = 1
GV_NombreArchivo = "registro.txt"


# configuraciones de logs
import logging
logging.basicConfig(
level=logging.INFO,
format='Fecha:%(asctime)s - User:%(name)s - %(message)s - %(levelname)s',
filename = 'Register_Log.log',
filemode =  'a'
)

# declarar funciones
def F_Leer(LV_NombreArchivo):
    with open(LV_NombreArchivo, "rb") as f:
        for linea in f:
            print("\n",linea.decode("utf-8"),end = "\n")

def F_Escribir(LV_NombreArchivo):
    with open(LV_NombreArchivo, "a") as file_object:
        LV_Nombre = str(input("ingrese nombre completo:\n"))
        LV_ID = int(input("ingrese id:\n"))
        file_object.write("nombre: {} ".format(LV_Nombre))
        file_object.write("ID:{}\n".format(LV_ID))

def F_Buscar(LV_NombreArchivo, ID):
  ID = input("\ningrese la id del registro a buscar: ")
 
  with open(LV_NombreArchivo, "r") as f:
  
    lineas = f.readlines()
    for linea in lineas:
      if ID in linea:
        print(linea)
        break
    else:
      print("La id no existe en el archivo")
           
def F_Borrar(LV_NombreArchivo, valor):
    valor = input("\ningrese la id del registro a borrar: ")

    with open(LV_NombreArchivo, 'r') as f:
        lineas = f.readlines()
    with open(LV_NombreArchivo, 'w') as f:
        for linea in lineas:
            if valor not in linea:
                f.write(linea)

def F_Ordenar():
    print("hola")
  

# activar y desactivar log
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
while GV_Seleccion != 0:
    GV_Seleccion = int(input("\nQue Operaacion Desea Relizar El Dia De Hoy?\n 1=leer|2=buscar|3=escribir|4=borrar|0=salir :"))
    if(GV_Seleccion == 1):
        F_Leer(GV_NombreArchivo)
    elif(GV_Seleccion == 2):
        F_Buscar(GV_NombreArchivo, 0)
    elif(GV_Seleccion == 3):
        F_Escribir(GV_NombreArchivo)
    elif(GV_Seleccion == 4):
        F_Borrar(GV_NombreArchivo,0)
    elif(GV_Seleccion == 0):
        print("Adios")
    else:
        logging.error("Caracter invalido.")
        print("Caracter invalido.")



