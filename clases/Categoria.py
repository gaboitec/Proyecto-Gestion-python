class Categoria:
    def __init__(self, id_categoria, nombre):
        self.id = id_categoria
        self.nombre = nombre

    @classmethod
    def from_linea(cls, linea):
        return cls(*linea.split("|"))

    def to_linea(self):
        return f"{self.id}|{self.nombre}"
