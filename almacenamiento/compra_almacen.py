from clases.Compra import Compra

class CompraRepository:
    def __init__(self, archivo_path):
        self.archivo_path = archivo_path
        self.compras = self._cargar()

    def _cargar(self):
        compras = {}
        try:
            with open(self.archivo_path, "r", encoding="utf-8") as archivo:
                for linea in archivo:
                    compra = Compra.from_linea(linea.strip())
                    compras[compra.id] = compra
        except FileNotFoundError:
            pass
        return compras

    def guardar(self):
        with open(self.archivo_path, "w", encoding="utf-8") as archivo:
            for compra in self.compras.values():
                archivo.write(compra.to_linea() + "\n")

    def agregar(self, compra):
        self.compras[compra.id] = compra
        self.guardar()

    def obtener_por_id(self, id_compra):
        return self.compras.get(id_compra)

    def obtener_todos(self):
        return list(self.compras.values())
