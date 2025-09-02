from clases.Cliente import Cliente

class ClienteRepo:
    def __init__(self, archivo_path):
        self.archivo_path = archivo_path
        self.clientes = self._cargar()

    def _cargar(self):
        clientes = {}
        try:
            with open(self.archivo_path, "r", encoding="utf-8") as archivo:
                for linea in archivo:
                    cliente = Cliente.from_linea(linea.strip())
                    clientes[cliente.nit] = cliente
        except FileNotFoundError:
            pass
        return clientes

    def guardar(self):
        with open(self.archivo_path, "w", encoding="utf-8") as archivo:
            for cliente in self.clientes.values():
                archivo.write(cliente.to_linea() + "\n")

    def agregar(self, cliente):
        self.clientes[cliente.nit] = cliente
        self.guardar()

    def obtener_por_nit(self, nit):
        return self.clientes.get(nit)

    def obtener_todos(self):
        return list(self.clientes.values())
