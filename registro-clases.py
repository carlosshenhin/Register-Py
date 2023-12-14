# bibliotecas
from pathlib import Path
import pickle
import logging


# manejador de archivo para guardar los logs en un archivo de texto
logger = logging.getLogger("MiApp")
logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler("registro.log")
file_handler.setFormatter(logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")) # Puedes cambiar el formato de los logs según tus preferencias

# clase con atributos y metodos
class Usuario:
    def __init__(self, nombre, apellido, ID):
        self.nombre = nombre
        self.apellido = apellido
        self.ID = ID

    def __str__(self):
        # Definimos un método para mostrar los datos del usuario de forma amigable
        return f"{self.nombre} {self.apellido} ({self.ID})"

#declaracion de funciones
def registrar_usuario():
    nombre = input("Ingrese el nombre del usuario: ")
    apellido = input("Ingrese el apellido del usuario: ")
    ID = input("Ingrese el ID del usuario: ")
   
    usuario = Usuario(nombre, apellido, ID)

    archivo = open("usuarios.bin", "ab")
    pickle.dump(usuario, archivo)
    
    archivo.close()
    logger.info("Escritura en el archivo")
    print(f"El usuario {usuario} ha sido registrado con éxito.")

def leer_usuarios():
    
    archivo = open("usuarios.bin", "rb")
   
    #lista para almacenar usuarios
    usuarios = []

    #ciclo while para leer todos los objetos del archivo
    while True:
        try:
            #función pickle.load() para cargar un objeto desde el archivo
            usuario = pickle.load(archivo)

            # Añadimos el objeto a la lista de usuarios
            usuarios.append(usuario)

        except EOFError:
            break
    
    archivo.close()

    if len(usuarios) is 0:
        print(f"No se encontró ningún usuario")
        logger.error("No se pudo leer el registro o registro vacio")
    else:
        print(f"Se han encontrado {len(usuarios)} usuarios registrados:")
        for usuario in usuarios:
            print(usuario)
            logger.info("Lectura del archivo")

def buscar_usuario():
    ID = input("Ingrese el ID del usuario a buscar: ")
    
    archivo = open("usuarios.bin", "rb")
  

    #variable para almacenar el usuario encontrado (o None si no se encuentra)
    usuario_encontrado = None

    #un ciclo while para buscar el usuario en el archivo
    while True:
        try:
            
            usuario = pickle.load(archivo)
            # Comparamos el ID del objeto con el ID ingresado
            if usuario.ID == ID:
                # Si son iguales, guardamos el objeto en la variable usuario_encontrado
                usuario_encontrado = usuario
                # Salimos del ciclo
                break

        except EOFError:
            break

    archivo.close()
    if usuario_encontrado is None:
        print(f"No se encontró ningún usuario con el ID {ID}.")
    else:
        logger.info("Busqueda en el archivo")
        print(f"Se encontró el usuario con el ID {ID}:")
        print(usuario_encontrado)

def borrar_usuario():

    ID = input("Ingrese el ID del usuario a borrar: ")

    archivo = open("usuarios.bin", "rb")


    #lista vacía para almacenar los usuarios que no se van a borrar
    usuarios = []
    #variable para almacenar el usuario borrado (o None si no se encuentra)
    usuario_borrado = None

   
    while True:
        try:
            usuario = pickle.load(archivo)
            # Comparamos el ID del objeto con el ID ingresado
            if usuario.ID == ID:
                # Si son iguales, guardamos el objeto en la variable usuario_borrado
                usuario_borrado = usuario
            else:
                # Si no son iguales, añadimos el objeto a la lista de usuarios
                usuarios.append(usuario)

        except EOFError:
            break
    
    archivo.close()
   
    if usuario_borrado is None:
        print(f"No se encontró ningún usuario con el ID {ID}.")
    else:
        logger.info("Borrado en el archivo")
        print(f"El usuario {usuario_borrado} ha sido borrado con éxito.")

        # Abrimos el archivo binario en modo write (para sobreescribir)
        archivo = open("usuarios.bin", "wb")
        # Usamos un ciclo for para guardar los usuarios que no se borraron en el archivo
        for usuario in usuarios:
            # Usamos la función pickle.dump() para guardar el objeto usuario en el archivo
            pickle.dump(usuario, archivo)
       
        archivo.close()

def ordenar_usuarios():
   
    archivo = open("usuarios.bin", "rb")

    usuarios = []
  
    while True:
        try:
         
            usuario = pickle.load(archivo)
         
            usuarios.append(usuario)

        except EOFError:
            break
    
    archivo.close()
    # Ordenamos la lista de usuarios por el atributo ID usando una función lambda
    usuarios.sort(key=lambda u: u.ID)
    
    archivo = open("usuarios.bin", "wb")
   
    for usuario in usuarios:
        pickle.dump(usuario, archivo)
    archivo.close()

# variables globales
GV_Seleccion = 1
GV_Log_switch = 0

# crear archivo "usuarios" en caso de no exisir
myfile = Path("usuarios.bin")
myfile.touch(exist_ok=True)

# activar o desactivar log
while GV_Log_switch != 1 and GV_Log_switch != 2:
    GV_Log_switch = int(input("\nDesea activar el log de acciones?:1=si|2=no\n"))
    if GV_Log_switch == 1:
        LOGGING_ENABLED = True
        print("Logs activados")
    elif GV_Log_switch == 2:
        LOGGING_ENABLED = False
        print("Logs desactivados")
    else:
        print("valor no compatible")


# confirmar si el log esta activo o no y hacerlo funcionar
if LOGGING_ENABLED:
    logger.addHandler(file_handler)

# menu de funciones
while GV_Seleccion != 0:

    ordenar_usuarios()

    GV_Seleccion = int(input("\nQue Operaacion Desea Relizar El Dia De Hoy?\n 1=leer|2=buscar|3=escribir|4=borrar|0=salir :"))
    if(GV_Seleccion == 1):
        leer_usuarios()
    elif(GV_Seleccion == 2):
        buscar_usuario()
    elif(GV_Seleccion == 3):
        registrar_usuario()
    elif(GV_Seleccion == 4):
        borrar_usuario()
    elif(GV_Seleccion == 0):
        print("Adios")
    else:
        print("Caracter invalido.")