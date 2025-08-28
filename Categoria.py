class Categoria:
    def __init__(self, codigo, nombre):
        self.__id = codigo
        self.__nombre = nombre

    def getCategoria(self):
        return {"id":self.__id, "nombre":self.__nombre}

    def setCategoria(self, codigo = None, nombre = None):
        if codigo:
            self.__id = codigo
        if nombre:
            self.__nombre = nombre

class Categorias:
    def __init__(self):
        self.__categorias = {}

    def addCategoria(self):
