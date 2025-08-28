class Producto:
    def __init__(self, codigo, nombre, precio, id_categoria, stock):
        self.__codigo = codigo
        self.__nombre = nombre
        self.__precio = precio
        self.__id_categoria = id_categoria
        self.__total_compras = 0
        self.__total_ventas = 0
        self.__stock = stock

    # RETORNA UN DICCIONARIO
    def getProducto(self):
        return {"codigo": self.__codigo, "nombre": self.__nombre, "precio": self.__precio, "id_categoria": self.__id_categoria, "total_compras":self.__total_compras, "total_ventas": self.__total_ventas,"stock": self.__stock}

    def setProducto(self, codigo=None, nombre=None, precio=None, id_categoria=None, total_compras=None, total_ventas=None, stock=None):
        if codigo:
            self.__codigo = codigo
        if nombre:
            self.__nombre = nombre
        if precio:
            self.__precio = precio
        if id_categoria:
            self.__id_categoria = id_categoria
        if total_compras:
            self.__total_compras = total_compras
        if total_ventas:
            self.__total_ventas = total_ventas
        if stock:
            self.__stock = stock


class Productos:
    def __init__(self):
        self.__productos = {}

    def addProducto(self, categorias):
        idp = input("IDProducto: ")
        nombre = input("Nombre producto: ")
        precio = float(input("Precio: "))
        idc = input("IDCategoria del producto: ")

        if idc not in categorias:
            print("Error: La categoría no existe. Agrega primero la categoría.")
        else:
            stock = int(input("Stock inicial: "))
            self.__productos[idp] = Producto(idp, nombre, precio, idc, stock)
            print("...Producto agregado")

    def mostrarProductos(self, categorias):
        print("PRODUCTOS:")
        for producto in self.__productos.values():
            productos = producto.getProductos()
            print(f"Codigo: {productos['codigo']} - Nombre: {productos['nombre']} - Precio: {productos['precio']} - Categoria: {categorias[productos['id_categoria']]} - Ventas: {productos['total_ventas']} - Compras: {productos['total_ventas']} - Stock: {productos['stock']}")

    def getProductos(self):
        return self.__productos