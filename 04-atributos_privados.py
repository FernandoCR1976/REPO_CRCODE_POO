#01 creamos la clase
class MiClase:
    def __init__(self): #02 Creamos el constructor de la clase
        self._atributo_privado = 42 #03 Definimos sus tributos

    #04 Creamos los metodos que vamos a necesitar de la clase
    def obtener_atributo(self):
        return self._atributo_privado
    
    def modificar_atributo(self,nuevo_valor):
        self._atributo_privado = nuevo_valor

#05 Instaciamos la clase
objeto = MiClase()

obejeto2 = MiClase()

objeto3 = MiClase()



#06 Probamos el funcionamiento de los metodos y atributos para la instacia de la clase
print(objeto._atributo_privado)
print(objeto.obtener_atributo())
objeto.modificar_atributo(100)
print(objeto.obtener_atributo())