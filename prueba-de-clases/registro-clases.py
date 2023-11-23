# Definir una clase llamada Usuario
class Usuario:
    # Inicializar la clase con los atributos nombre, edad y correo
    def __init__(self, nombre, edad, correo):
        self.nombre = nombre
        self.edad = edad
        self.correo = correo
    
    # Definir un método para mostrar los datos del usuario
    def mostrar(self):
        print(f"Nombre: {self.nombre}")
        print(f"Edad: {self.edad}")
        print(f"Correo: {self.correo}")

# Crear un objeto de la clase Usuario con los datos de un usuario
usuario1 = Usuario("Ana", 25, "ana@gmail.com")

# Guardar el objeto en un archivo usando el módulo pickle
import pickle
with open("usuario1.pkl", "wb") as archivo:
    pickle.dump(usuario1, archivo)

# Leer el objeto desde el archivo
with open("usuario1.pkl", "rb") as archivo:
    usuario1 = pickle.load(archivo)

# Imprimir los datos del usuario usando el método mostrar
usuario1.mostrar()

