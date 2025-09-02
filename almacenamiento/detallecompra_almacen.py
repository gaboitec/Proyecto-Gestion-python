from clases.DetalleCompra import DetalleCompra

class DetalleCompraRepo:
    def __init__(self, archivo_path):
        self.archivo_path = archivo_path
        self.detalles = self._cargar()

    def _cargar(self):
        detalles = {}
        try:
            with open(self.archivo_path, "r", encoding="utf-8") as archivo:
                for linea in archivo:
                    detalle = DetalleCompra.from_linea(linea.strip())
                    detalles[detalle.id] = detalle
        except FileNotFoundError:
            pass
        return detalles

    def guardar(self):
        with open(self.archivo_path, "w", encoding="utf-8") as archivo:
            for detalle in self.detalles.values():
                archivo.write(detalle.to_linea() + "\n")

    def agregar(self, detalle):
        self.detalles[detalle.id] = detalle
        self.guardar()

    def obtener_por_id(self, id_detalle):
        return self.detalles.get(id_detalle)

    def obtener_todos(self):
        return list(self.detalles.values())
