class Tienda:
    
    def __init__(self) -> None:
        self.clientes = []
        self.productos = {}

class Cliente:

    def __init__(self, apodo, celular):
        self.apodo = apodo
        self.celular = celular
        self.carrito = Carrito()

class Fiador(Cliente):

    def __init__(self, apodo, celular, valor_deuda):
        super().__init__(apodo, celular)
        self.valor_deuda = valor_deuda

class Normal(Cliente):

    def __init__(self, apodo, celular, valor_compra):
        super().__init__(apodo, celular)
        self.valor_compra = valor_compra

class Productos:

    def __init__(self,nombre, cantidad, valor):
        self.nombre = nombre
        self.cantidad = cantidad
        self.valor = valor

class Carrito:

    def __init__(self) -> None:
        self.productos = {} 