from clases.Cliente import Cliente

class Proveedor(Cliente):
    def __init__(self, nit, nombre, direccion, telefono, correo, empresa):
        super().__init__(nit, nombre, direccion, telefono, correo)
        self.empresa = empresa

    @classmethod
    def from_linea(cls, linea):
        return cls(*linea.split("|"))

    def to_linea(self):
        return f"{self.nit}|{self.nombre}|{self.direccion}|{self.telefono}|{self.correo}|{self.empresa}"
