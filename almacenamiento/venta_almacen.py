from clases.Venta import Venta

class VentaRepo:
    def __init__(self, archivo_path):
        self.archivo_path = archivo_path
        self.ventas = self._cargar()

    def _cargar(self):
        ventas = {}
        try:
            with open(self.archivo_path, "r", encoding="utf-8") as archivo:
                for linea in archivo:
                    venta = Venta.from_linea(linea.strip())
                    ventas[venta.id] = venta
        except FileNotFoundError:
            pass
        return ventas

    def guardar(self):
        with open(self.archivo_path, "w", encoding="utf-8") as archivo:
            for venta in self.ventas.values():
                archivo.write(venta.to_linea() + "\n")

    def agregar(self, venta):
        self.ventas[venta.id] = venta
        self.guardar()

    def obtener_por_id(self, id_venta):
        return self.ventas.get(id_venta)

    def obtener_todos(self):
        return list(self.ventas.values())
