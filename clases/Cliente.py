class Cliente:
    def __init__(self, nit, nombre, direccion, telefono, correo):
        self.nit = nit
        self.nombre = nombre
        self.direccion = direccion
        self.telefono = telefono
        self.correo = correo

    @classmethod
    def from_linea(cls, linea):
        return cls(*linea.split("|"))

    def to_linea(self):
        return f"{self.nit}|{self.nombre}|{self.direccion}|{self.telefono}|{self.correo}"
