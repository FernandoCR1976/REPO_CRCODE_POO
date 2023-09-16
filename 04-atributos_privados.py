class MiClase:
    def __init__(self):
        self._atributo_privado = 42

    def obtener_atributo(self):
        return self._atributo_privado
    
    def modificar_atributo(self,nuevo_valor):
        self._atributo_privado = nuevo_valor


objeto = MiClase()


print(objeto._atributo_privado)
print(objeto.obtener_atributo())
objeto.modificar_atributo(100)
print(objeto.obtener_atributo())