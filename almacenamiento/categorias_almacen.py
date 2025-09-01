# repositories/categoria_repository.py

from clases.Categoria import Categoria

class CategoriaRepository:
    def __init__(self, archivo_path):
        self.archivo_path = archivo_path
        self.categorias = self._cargar()

    def _cargar(self):
        categorias = {}
        try:
            with open(self.archivo_path, "r", encoding="utf-8") as archivo:
                for linea in archivo:
                    categoria = Categoria.from_linea(linea.strip())
                    categorias[categoria.id] = categoria
        except FileNotFoundError:
            pass
        return categorias

    def guardar(self):
        with open(self.archivo_path, "w", encoding="utf-8") as archivo:
            for categoria in self.categorias.values():
                archivo.write(categoria.to_linea() + "\n")

    def agregar(self, categoria):
        self.categorias[categoria.id] = categoria
        self.guardar()

    def obtener_por_id(self, id_categoria):
        return self.categorias.get(id_categoria)

    def obtener_todos(self):
        return list(self.categorias.values())
