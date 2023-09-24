#Crear la clase Persona con atributos y métodos privados. Los atributos _nombre y _edad son privados y solo deberían ser accedidos desde dentro de la clase. El método _es_mayor_de_edad es un método privado que verifica si la persona es mayor de edad. Los métodos públicos obtener_informacion y cambiar_edad permiten interactuar con los atributos privados de manera controlada.



#01 Craemos la clase

class Persona:
    def __init__(self,nombre,edad,sexo):
        self.__nombre = nombre
        self.__edad = edad
        self.sexo = sexo


    def _es_mayor_de_edad(self):
        return self.__edad >= 18


    def obtener_informacion(self):
        if self._es_mayor_de_edad():
            return f"{self.__nombre} es mayor de edad y es {self.sexo}."
        else:
            return  f"{self.__nombre} es menor de edad {self.sexo}."
        
    def cambiar_edad(self,nueva_edad):
        if nueva_edad >=0:
            self.__edad = nueva_edad

    def cambiar_nombre(self,nuevo_nombre):
        self.__nombre = nuevo_nombre



# creamos a persona1 y persona2 que son INSTANCIAS  de la clase Persona

persona1 = Persona("Randall",25,'Hombre')
persona2 = Persona("Daniel",32,'Hombre')

print(persona1.obtener_informacion())
persona2.cambiar_nombre('Jose')
print(persona2.obtener_informacion())

persona1.sexo = 'H'
persona1.__nombre = 'Alberto'
persona1.cambiar_nombre('Alberto')

print(persona1.obtener_informacion())


#print(persona1.__nombre)































