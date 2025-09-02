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
    print("\nInventario de productos:")
    for producto in producto_repo.obtener_todos():
        categoria = categoria_repo.obtener_por_id(producto.id_categoria)
        nombre_categoria = categoria.nombre if categoria else "Sin categoría"
        print(f"- {producto.nombre} | Precio: Q{producto.precio:.2f} | Stock: {producto.stock} | Categoría: {nombre_categoria}")

def registrar_producto(producto_repo, categoria_repo):
    print("\nRegistro de producto")
    id = input("ID: ")
    '''if producto_repo.obtener_por_id(id):
        print("Ya existe un producto con ese ID.")
        return'''
    nombre = input("Nombre: ")
    precio = float(input("Precio: "))
    id_categoria = input("ID Categoría: ")
    if not categoria_repo.obtener_por_id(id_categoria):
        print("Categoría no encontrada.")
        return
    stock = int(input("Stock: "))
    producto = Producto(id, nombre, precio, id_categoria,0, 0, stock)
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
    print("\nRegistro de cliente")
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

def registrar_venta(venta_repo, detalle_repo, producto_repo, cliente_repo, empleado_repo):
    print("\nRegistro de venta")
    id_venta = input("ID Venta: ")
    fecha = input("Fecha (dd/mm/yyyy): ")
    id_empleado = input("ID Empleado: ")
    nit_cliente = input("NIT Cliente: ")

    if not empleado_repo.obtener_por_id(id_empleado):
        print("Empleado no encontrado.")
        return
    if not cliente_repo.obtener_por_nit(nit_cliente):
        print("Cliente no encontrado.")
        return

    total = 0
    detalles = []

    while True:
        id_producto = input("ID Producto (o 'fin' para terminar): ")
        if id_producto.lower() == "fin":
            break
        producto = producto_repo.obtener_por_id(id_producto)
        if not producto:
            print("Producto no encontrado.")
            continue

        cantidad = int(input("Cantidad: "))
        if cantidad > producto.stock:
            print("Stock insuficiente.")
            continue

        subtotal = cantidad * producto.precio
        producto.stock -= cantidad
        producto.total_ventas += cantidad
        producto_repo.guardar()

        id_detalle = f"D{len(detalle_repo.detalles)+1:03}"
        detalle = DetalleVenta(id_detalle, id_venta, cantidad, id_producto, subtotal, producto.stock)
        detalle_repo.agregar(detalle)
        detalles.append(detalle)
        total += subtotal

    venta = Venta(id_venta, fecha, id_empleado, nit_cliente, total)
    venta_repo.agregar(venta)
    print(f"Venta registrada. Total: Q{total:.2f}")

def registrar_compra(compra_repo, detalle_repo, producto_repo, proveedor_repo, empleado_repo):
    print("\n📥 Registro de compra")
    id_compra = input("ID Compra: ")
    fecha = input("Fecha ingreso (dd/mm/yyyy): ")
    id_empleado = input("ID Empleado: ")
    nit_proveedor = input("NIT Proveedor: ")

    if not empleado_repo.obtener_por_id(id_empleado):
        print("Empleado no encontrado.")
        return
    if not proveedor_repo.obtener_por_nit(nit_proveedor):
        print("Proveedor no encontrado.")
        return

    total = 0
    detalles = []

    while True:
        id_producto = input("ID Producto (o 'fin' para terminar): ")
        if id_producto.lower() == "fin":
            break
        producto = producto_repo.obtener_por_id(id_producto)
        if not producto:
            print("Producto no encontrado.")
            continue

        cantidad = int(input("Cantidad: "))
        fecha_caducidad = input("Fecha de caducidad (dd/mm/yyyy): ")
        subtotal = cantidad * producto.precio

        producto.stock += cantidad
        producto.total_compras += cantidad
        producto_repo.guardar()

        id_detalle = f"DC{len(detalle_repo.detalles)+1:03}"
        detalle = DetalleCompra(id_detalle, id_compra, cantidad, id_producto, subtotal, fecha_caducidad)
        detalle_repo.agregar(detalle)
        detalles.append(detalle)
        total += subtotal

    compra = Compra(id_compra, fecha, id_empleado, nit_proveedor, total)
    compra_repo.agregar(compra)
    print(f"Compra registrada. Total: Q{total:.2f}")

def mostrar_ventas(venta_repo, detalle_repo, cliente_repo, empleado_repo, producto_repo):
    print("\nHistorial de ventas:")
    for venta in venta_repo.obtener_todos():
        cliente = cliente_repo.obtener_por_nit(venta.nit_cliente)
        empleado = empleado_repo.obtener_por_id(venta.id_empleado)
        print(f"\nVenta ID: {venta.id} | Fecha: {venta.fecha} | Total: Q{venta.total:.2f}")
        print(f"Cliente: {cliente.nombre if cliente else 'Desconocido'}")
        print(f"Empleado: {empleado.nombre if empleado else 'Desconocido'}")
        print("Detalles:")
        for detalle in detalle_repo.obtener_todos():
            if detalle.id_venta == venta.id:
                producto = producto_repo.obtener_por_id(detalle.id_producto)
                nombre_producto = producto.nombre if producto else "Producto desconocido"
                print(f"  - {nombre_producto} | Cantidad: {detalle.cantidad} | Subtotal: Q{detalle.subtotal:.2f}")

def mostrar_compras(compra_repo, detalle_repo, proveedor_repo, empleado_repo, producto_repo):
    print("\nHistorial de compras:")
    for compra in compra_repo.obtener_todos():
        proveedor = proveedor_repo.obtener_por_nit(compra.nit_proveedor)
        empleado = empleado_repo.obtener_por_id(compra.id_empleado)
        print(f"\nCompra ID: {compra.id} | Fecha: {compra.fecha_ingreso} | Total: Q{compra.total:.2f}")
        print(f"Proveedor: {proveedor.nombre if proveedor else 'Desconocido'}")
        print(f"Empleado: {empleado.nombre if empleado else 'Desconocido'}")
        print("Detalles:")
        for detalle in detalle_repo.obtener_todos():
            if detalle.id_venta == compra.id:
                producto = producto_repo.obtener_por_id(detalle.id_producto)
                nombre_producto = producto.nombre if producto else "Producto desconocido"
                print(f"  - {nombre_producto} | Cantidad: {detalle.cantidad} | Subtotal: Q{detalle.subtotal:.2f} | Caducidad: {detalle.fecha_caducidad}")


def menu():
    producto_repo = ProductoRepository("archivos/productos.txt")
    categoria_repo = CategoriaRepository("archivos/categorias.txt")
    cliente_repo = ClienteRepository("archivos/clientes.txt")
    proveedor_repo = ProveedorRepository("archivos/proveedores.txt")
    empleado_repo = EmpleadoRepository("archivos/empleados.txt")
    venta_repo = VentaRepository("archivos/ventas.txt")
    detalle_venta_repo = DetalleVentaRepository("archivos/detalle_ventas.txt")
    compra_repo = CompraRepository("archivos/compras.txt")
    detalle_compra_repo = DetalleCompraRepository("archivos/detalle_compras.txt")

    opciones = {
        "1": lambda: mostrar_productos(producto_repo, categoria_repo),
        "2": lambda: registrar_producto(producto_repo, categoria_repo),
        "3": lambda: registrar_categoria(categoria_repo),
        "4": lambda: registrar_cliente(cliente_repo),
        "5": lambda: registrar_proveedor(proveedor_repo),
        "6": lambda: registrar_empleado(empleado_repo),
        "7": lambda: registrar_venta(venta_repo, detalle_venta_repo, producto_repo, cliente_repo, empleado_repo),
        "8": lambda: registrar_compra(compra_repo, detalle_compra_repo, producto_repo, proveedor_repo, empleado_repo),
        "9": lambda: mostrar_ventas(venta_repo, detalle_venta_repo, cliente_repo, empleado_repo, producto_repo),
        "10": lambda: mostrar_compras(compra_repo, detalle_compra_repo, proveedor_repo, empleado_repo, producto_repo),
        "0": lambda: print("Saliendo del sistema.")
    }

    while True:
        print("\nMenú principal")
        print("1. Mostrar productos")
        print("2. Registrar producto")
        print("3. Registrar categoría")
        print("4. Registrar cliente")
        print("5. Registrar proveedor")
        print("6. Registrar empleado")
        print("7. Registrar venta")
        print("8. Registrar compra")
        print("9. Mostrar ventas")
        print("10. Mostrar compras")
        print("0. Salir")
        opcion = input("Seleccione una opción: ")

        accion = opciones.get(opcion)
        if accion:
            accion()
            if opcion == "0":
                break
        else:
            print("Opción inválida.")

if __name__ == "__main__":
    menu()
