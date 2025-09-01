class Producto:
    def __init__(self, id_producto, nombre, precio, id_categoria, total_compras, total_ventas, stock):
        self.id = id_producto
        self.nombre = nombre
        self.precio = float(precio)
        self.id_categoria = id_categoria
        self.total_compras = int(total_compras)
        self.total_ventas = int(total_ventas)
        self.stock = int(stock)

    @classmethod
    def from_linea(cls, linea):
        partes = linea.split("|")
        return cls(*partes)

    def to_linea(self):
        return f"{self.id}|{self.nombre}|{self.precio}|{self.id_categoria}|{self.total_compras}|{self.total_ventas}|{self.stock}"
