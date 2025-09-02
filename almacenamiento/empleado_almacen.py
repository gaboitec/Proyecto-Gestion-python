from clases.Empleado import Empleado

class EmpleadoRepo:
    def __init__(self, archivo_path):
        self.archivo_path = archivo_path
        self.empleados = self._cargar()

    def _cargar(self):
        empleados = {}
        try:
            with open(self.archivo_path, "r", encoding="utf-8") as archivo:
                for linea in archivo:
                    empleado = Empleado.from_linea(linea.strip())
                    empleados[empleado.id] = empleado
        except FileNotFoundError:
            pass
        return empleados

    def guardar(self):
        with open(self.archivo_path, "w", encoding="utf-8") as archivo:
            for empleado in self.empleados.values():
                archivo.write(empleado.to_linea() + "\n")

    def agregar(self, empleado):
        self.empleados[empleado.id] = empleado
        self.guardar()

    def obtener_por_id(self, id_empleado):
        return self.empleados.get(id_empleado)

    def obtener_todos(self):
        return list(self.empleados.values())
