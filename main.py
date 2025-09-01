# main.py

from repositories.producto_repository import ProductoRepository
from repositories.categoria_repository import CategoriaRepository
from models.producto import Producto
from models.categoria import Categoria

def mostrar_productos(producto_repo, categoria_repo):
    productos = producto_repo.obtener_todos()
    if not productos:
        print("\nNo hay productos registrados.")
        return

    print("\n📦 Inventario de productos:")
    for producto in productos:
        categoria = categoria_repo.obtener_por_id(producto.id_categoria)
        nombre_categoria = categoria.nombre if categoria else "Sin categoría"
        print(f"- {producto.nombre} | Precio: Q{producto.precio:.2f} | Stock: {producto.stock} | Categoría: {nombre_categoria}")

def agregar_producto(producto_repo, categoria_repo):
    print("\n🆕 Registro de nuevo producto")
    id_producto = input("ID del producto: ")
    if producto_repo.obtener_por_id(id_producto):
        print("❌ Ya existe un producto con ese ID.")
        return

    nombre = input("Nombre del producto: ")
    precio = float(input("Precio: "))
    id_categoria = input("ID de la categoría: ")
    if not categoria_repo.obtener_por_id(id_categoria):
        print("⚠️ Categoría no encontrada. Registra la categoría primero.")
        return

    stock = int(input("Stock inicial: "))
    producto = Producto(id_producto, nombre, precio, id_categoria, stock)
    producto_repo.agregar(producto)
    print("✅ Producto agregado con éxito.")

def agregar_categoria(categoria_repo):
    print("\n🆕 Registro de nueva categoría")
    id_categoria = input("ID de la categoría: ")
    if categoria_repo.obtener_por_id(id_categoria):
        print("❌ Ya existe una categoría con ese ID.")
        return

    nombre = input("Nombre de la categoría: ")
    categoria = Categoria(id_categoria, nombre)
    categoria_repo.agregar(categoria)
    print("✅ Categoría agregada con éxito.")

def menu():
    producto_repo = ProductoRepository("data/productos.txt")
    categoria_repo = CategoriaRepository("data/categorias.txt")

    opciones = {
        "1": lambda: mostrar_productos(producto_repo, categoria_repo),
        "2": lambda: agregar_producto(producto_repo, categoria_repo),
        "3": lambda: agregar_categoria(categoria_repo),
        "0": lambda: print("👋 Saliendo del sistema.")
    }

    while True:
        print("\n📋 Menú principal")
        print("1. Mostrar productos")
        print("2. Agregar producto")
        print("3. Agregar categoría")
        print("0. Salir")
        opcion = input("Seleccione una opción: ")

        accion = opciones.get(opcion)
        if accion:
            accion()
            if opcion == "0":
                break
        else:
            print("❌ Opción inválida. Intente de nuevo.")

if __name__ == "__main__":
    menu()
