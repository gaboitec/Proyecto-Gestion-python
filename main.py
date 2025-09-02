from almacenamiento.productos_almacen import ProductoRepo as ProductoRepository
from almacenamiento.categorias_almacen import CategoriaRepo as CategoriaRepository
from almacenamiento.clientes_almacen import ClienteRepo as ClienteRepository
from almacenamiento.proveedor_almacen import ProveedorRepo as ProveedorRepository
from almacenamiento.empleado_almacen import EmpleadoRepo as EmpleadoRepository
from almacenamiento.venta_almacen import VentaRepo as VentaRepository
from almacenamiento.detalleventa_almacen import DetalleVentaRepo as DetalleVentaRepository
from almacenamiento.compra_almacen import CompraRepo as CompraRepository
from almacenamiento.detallecompra_almacen import DetalleCompraRepo as DetalleCompraRepository

from clases.Producto import Producto
from clases.Categoria import Categoria
from clases.Cliente import Cliente
from clases.Proveedor import Proveedor
from clases.Empleado import Empleado
from clases.Venta import Venta
from clases.DetalleVenta import DetalleVenta
from clases.Compra import Compra
from clases.DetalleCompra import DetalleCompra

def mostrar_productos(producto_repo, categoria_repo):
    print("\n📦 Inventario de productos:")
    for producto in producto_repo.obtener_todos():
        categoria = categoria_repo.obtener_por_id(producto.id_categoria)
        nombre_categoria = categoria.nombre if categoria else "Sin categoría"
        print(f"- {producto.nombre} | Precio: Q{producto.precio:.2f} | Stock: {producto.stock} | Categoría: {nombre_categoria}")

def registrar_producto(producto_repo, categoria_repo):
    print("\nRegistro de producto")
    id = input("ID: ")
    if producto_repo.obtener_por_id(id):
        print("Ya existe un producto con ese ID.")
        return
    nombre = input("Nombre: ")
    precio = float(input("Precio: "))
    id_categoria = input("ID Categoría: ")
    if not categoria_repo.obtener_por_id(id_categoria):
        print("⚠Categoría no encontrada.")
        return
    stock = int(input("Stock: "))
    producto = Producto(id, nombre, precio, id_categoria, stock)
    producto_repo.agregar(producto)
    print("Producto registrado.")

def registrar_categoria(categoria_repo):
    print("\nRegistro de categoría")
    id = input("ID Categoría: ")
    if categoria_repo.obtener_por_id(id):
        print("Ya existe esa categoría.")
        return
    nombre = input("Nombre: ")
    categoria = Categoria(id, nombre)
    categoria_repo.agregar(categoria)
    print("Categoría registrada.")

def registrar_cliente(cliente_repo):
    print("\n🆕 Registro de cliente")
    nit = input("NIT: ")
    if cliente_repo.obtener_por_nit(nit):
        print("Cliente ya existe.")
        return
    nombre = input("Nombre: ")
    direccion = input("Dirección: ")
    telefono = input("Teléfono: ")
    correo = input("Correo: ")
    cliente = Cliente(nit, nombre, direccion, telefono, correo)
    cliente_repo.agregar(cliente)
    print("Cliente registrado.")

def registrar_proveedor(proveedor_repo):
    print("\nRegistro de proveedor")
    nit = input("NIT: ")
    if proveedor_repo.obtener_por_nit(nit):
        print("Proveedor ya existe.")
        return
    nombre = input("Nombre: ")
    direccion = input("Dirección: ")
    telefono = input("Teléfono: ")
    correo = input("Correo: ")
    empresa = input("Empresa: ")
    proveedor = Proveedor(nit, nombre, direccion, telefono, correo, empresa)
    proveedor_repo.agregar(proveedor)
    print("Proveedor registrado.")

def registrar_empleado(empleado_repo):
    print("\nRegistro de empleado")
    id = input("ID Empleado: ")
    if empleado_repo.obtener_por_id(id):
        print("Empleado ya existe.")
        return
    nombre = input("Nombre: ")
    direccion = input("Dirección: ")
    telefono = input("Teléfono: ")
    correo = input("Correo: ")
    puesto = input("Puesto: ")
    empleado = Empleado(id, nombre, direccion, telefono, correo, puesto)
    empleado_repo.agregar(empleado)
    print("Empleado registrado.")

def menu():
    producto_repo = ProductoRepository("data/productos.txt")
    categoria_repo = CategoriaRepository("data/categorias.txt")
    cliente_repo = ClienteRepository("data/clientes.txt")
    proveedor_repo = ProveedorRepository("data/proveedores.txt")
    empleado_repo = EmpleadoRepository("data/empleados.txt")
    venta_repo = VentaRepository("data/ventas.txt")
    detalle_venta_repo = DetalleVentaRepository("data/detalle_ventas.txt")
    compra_repo = CompraRepository("data/compras.txt")
    detalle_compra_repo = DetalleCompraRepository("data/detalle_compras.txt")

    opciones = {
        "1": lambda: mostrar_productos(producto_repo, categoria_repo),
        "2": lambda: registrar_producto(producto_repo, categoria_repo),
        "3": lambda: registrar_categoria(categoria_repo),
        "4": lambda: registrar_cliente(cliente_repo),
        "5": lambda: registrar_proveedor(proveedor_repo),
        "6": lambda: registrar_empleado(empleado_repo),
        "0": lambda: print("👋 Saliendo del sistema.")
    }

    while True:
        print("\n📋 Menú principal")
        print("1. Mostrar productos")
        print("2. Registrar producto")
        print("3. Registrar categoría")
        print("4. Registrar cliente")
        print("5. Registrar proveedor")
        print("6. Registrar empleado")
        print("0. Salir")
        opcion = input("Seleccione una opción: ")

        accion = opciones.get(opcion)
        if accion:
            accion()
            if opcion == "0":
                break
        else:
            print("❌ Opción inválida.")

if __name__ == "__main__":
    menu()
