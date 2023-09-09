#crear una clase Persona cuyos atributos son nombre, apellidos, edad, sexo e identificación
#crear un metodo que imprima el nombre completo de la persona
#crear un metodo que imprima el apellido, la edad y el sexo
#crear un metodo que imprima el apellido, el nombre

class Persona:
    def __init__(self,nombre, apellidos, edad, sexo, id):
        self.name = nombre
        self.lastname = apellidos
        self.age = edad
        self.gender = sexo
        self.id = id

    def nombre_completo(self):
        return f'El nombre del usuario es {self.name} {self.lastname}'
    
    def info_persona(self):
        return f'La información del usuario es {self.lastname}, {self.age} años y su identificación es: {self.id}'
    
    def apellido_nombre(self):
        print(f'El nombre del usuario es {self.lastname} {self.name}')



#tmpPersona = Persona('Fernando','Corrales',47,'Masculino',123)

def ingreso_datos():
    global persona1 

    nombre = input('Ingrese su nombre: ')
    apellidos = input('Ingrese sus apellidos: ')
    edad = float(input('ingrese su edad: '))
    sexo = input('Ingrese su genero: ')
    id = input('Ingrese su identificación: ')

    persona1 = Persona(nombre,apellidos,edad,sexo,id)

    return nombre,apellidos,edad,sexo,id

nombre,apellidos,edad,sexo,id = ingreso_datos()
tmpPersona = Persona(nombre,apellidos,edad,sexo,id)

tmpPersona.apellido_nombre()
persona1.apellido_nombre()