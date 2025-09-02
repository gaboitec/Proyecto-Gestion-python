from clases.Producto import Producto

class ProductoRepo:
    def __init__(self, archivo_path):
        self.archivo_path = archivo_path
        self.productos = self._cargar()

    def _cargar(self):
        productos = {}
        try:
            with open(self.archivo_path, "r", encoding="utf-8") as archivo:
                for linea in archivo:
                    producto = Producto.from_linea(linea.strip())
                    productos[producto.id] = producto
        except FileNotFoundError:
            pass
        return productos

    def guardar(self):
        with open(self.archivo_path, "w", encoding="utf-8") as archivo:
            for producto in self.productos.values():
                archivo.write(producto.to_linea() + "\n")

    def agregar(self, producto):
        self.productos[producto.id] = producto
        self.guardar()

    def eliminar(self, id_producto):
        if id_producto in self.productos:
            del self.productos[id_producto]
            self.guardar()

    def obtener_por_id(self, id_producto):
        return self.productos[id_producto]

    def obtener_todos(self):
        return list(self.productos.values())
