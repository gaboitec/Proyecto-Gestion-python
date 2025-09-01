class Compra:
    def __init__(self, id_compra, fecha_ingreso, id_empleado, nit_proveedor, total):
        self.id = id_compra
        self.fecha_ingreso = fecha_ingreso
        self.id_empleado = id_empleado
        self.nit_proveedor = nit_proveedor
        self.total = float(total)

    @classmethod
    def from_linea(cls, linea):
        return cls(*linea.split("|"))

    def to_linea(self):
        return f"{self.id}|{self.fecha_ingreso}|{self.id_empleado}|{self.nit_proveedor}|{self.total}"
