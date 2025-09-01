class DetalleVenta:
    def __init__(self, id_detalle, id_venta, cantidad, id_producto, subtotal, stock):
        self.id = id_detalle
        self.id_venta = id_venta
        self.cantidad = int(cantidad)
        self.id_producto = id_producto
        self.subtotal = float(subtotal)
        self.stock = int(stock)

    @classmethod
    def from_linea(cls, linea):
        return cls(*linea.split("|"))

    def to_linea(self):
        return f"{self.id}|{self.id_venta}|{self.cantidad}|{self.id_producto}|{self.subtotal}|{self.stock}"
