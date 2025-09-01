class Empleado:
    def __init__(self, id_empleado, nombre, direccion, telefono, correo, puesto):
        self.id = id_empleado
        self.nombre = nombre
        self.direccion = direccion
        self.telefono = telefono
        self.correo = correo
        self.puesto = puesto

    @classmethod
    def from_linea(cls, linea):
        return cls(*linea.split("|"))

    def to_linea(self):
        return f"{self.id}|{self.nombre}|{self.direccion}|{self.telefono}|{self.correo}|{self.puesto}"
