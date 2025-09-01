class Venta:
    def __init__(self, id_venta, fecha, id_empleado, nit_cliente, total):
        self.id = id_venta
        self.fecha = fecha
        self.id_empleado = id_empleado
        self.nit_cliente = nit_cliente
        self.total = float(total)

    @classmethod
    def from_linea(cls, linea):
        return cls(*linea.split("|"))

    def to_linea(self):
        return f"{self.id}|{self.fecha}|{self.id_empleado}|{self.nit_cliente}|{self.total}"
