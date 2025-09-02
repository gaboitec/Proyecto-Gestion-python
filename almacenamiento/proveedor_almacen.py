from clases.Proveedor import Proveedor

class ProveedorRepo:
    def __init__(self, archivo_path):
        self.archivo_path = archivo_path
        self.proveedores = self._cargar()

    def _cargar(self):
        proveedores = {}
        try:
            with open(self.archivo_path, "r", encoding="utf-8") as archivo:
                for linea in archivo:
                    proveedor = Proveedor.from_linea(linea.strip())
                    proveedores[proveedor.nit] = proveedor
        except FileNotFoundError:
            pass
        return proveedores

    def guardar(self):
        with open(self.archivo_path, "w", encoding="utf-8") as archivo:
            for proveedor in self.proveedores.values():
                archivo.write(proveedor.to_linea() + "\n")

    def agregar(self, proveedor):
        self.proveedores[proveedor.nit] = proveedor
        self.guardar()

    def obtener_por_nit(self, nit):
        return self.proveedores.get(nit)

    def obtener_todos(self):
        return list(self.proveedores.values())
