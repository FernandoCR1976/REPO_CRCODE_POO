#crear una aplicacion que registe un alumno y sus calificaciones del año, que guarde la información en un arreglo y que pueda mostrar la informacion de todos los alumnos con sus notas y promedio de notas


#Definir las clases

class Alumno:
    #Definimos el constructor
    def __init__(self, nombre):
        self.nombre = nombre
        self.calificaciones = []

    #Definición de los métodos de la clase

    def agregar_calificaciones(self,calificacion):
        self.calificaciones.append(calificacion)

    def calcular_promedio(self):
        if len(self.calificaciones)==0:
            return 0
        else:
            return sum(self.calificaciones)/len(self.calificaciones)



class RegistroAlumnos:
    def __init__(self):
        self.alumnos = []

    #Definir metodos
    def agregar_alumno(self,nombre):
        alumno = Alumno(nombre)
        self.alumnos.append(alumno)

    def buscar_alumno(self,nombre):
        for alumno in self.alumnos:
            if alumno.nombre == nombre:
                return alumno
        return None
    
    def mostrar_informacion(self):
        for alumno in self.alumnos:
            print(f'Nombre: {alumno.nombre}')
            print("Calificaciones: ", alumno.calificaciones)
            print(f'Promedio de notas {alumno.calcular_promedio()}')
            print("\n")


registro = RegistroAlumnos()

while True:
    print("1. Agregar Alumno")
    print("2. Agregar calificación Alumno")
    print("3. Mostrar Información de todos los Alumnos")
    print("4. Salir")

    opcion = int(input("Selecciones una opción"))

    if opcion == 1:
        nombre = input("Agregue el nombre del Alumno: ")
        registro.agregar_alumno(nombre)

    elif opcion ==2:
        nombre = input("Ingrese el nombre del Alumno: ")
        alumno = registro.buscar_alumno(nombre)
        if alumno:
            calificacion = float(input("Ingrese la calificación: "))
            alumno.agregar_calificaciones(calificacion)
        else:
            print("Alumno no fue encontrado")

    elif opcion == 3:
        registro.mostrar_informacion()

    elif opcion == 4:
        break

    else:
        print("opcion no es valida")






