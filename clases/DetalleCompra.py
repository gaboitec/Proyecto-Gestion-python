class DetalleCompra:
    def __init__(self, id_detalle, id_venta, cantidad, id_producto, subtotal, fecha_caducidad):
        self.id = id_detalle
        self.id_venta = id_venta
        self.cantidad = int(cantidad)
        self.id_producto = id_producto
        self.subtotal = float(subtotal)
        self.fecha_caducidad = fecha_caducidad

    @classmethod
    def from_linea(cls, linea):
        return cls(*linea.split("|"))

    def to_linea(self):
        return f"{self.id}|{self.id_venta}|{self.cantidad}|{self.id_producto}|{self.subtotal}|{self.fecha_caducidad}"
