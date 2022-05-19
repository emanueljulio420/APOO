class Tienda:
    
    def __init__(self) -> None:
        self.clientes = []
        self.dataproductos = {}

    def modificar_precio(self, nombre, precio):
        try:
            if nombre in self.dataproductos.keys():
                self.dataproductos[nombre].valor = precio
                print('\n---------------------------')
                print('Precio cambiado correctamente')
                print('---------------------------\n')
            else:
                raise KeyError()
        except KeyError:
            print('\n---------------------------')
            print('   Producto no existente   ')
            print('---------------------------\n')

    def agragar_productos(self, nombre, cantidad, valor):
        if nombre in self.dataproductos.keys():
            print('\n---------------------------')
            print('   Producto ya existente   ')
            print('---------------------------\n') 
        else:
            self.dataproductos[nombre] = Productos(nombre,cantidad,valor)
            print('\n---------------------------')
            print('Producto agregado correctamente')
            print('---------------------------\n')           
    
    def eliminar_producto(self,nombre):
        try:
            del self.dataproductos[nombre]
            print('\n---------------------------')
            print('Producto eliminado correctamente')
            print('---------------------------\n')
        except KeyError:
            print('\n---------------------------')
            print('   Producto no existente   ')
            print('---------------------------\n')
    
    def imprimir_productos(self):
        print('\n--------------Productos--------------\n')
        for i in self.dataproductos.keys():
            print('\n---------------------------')
            print(f'nombre: {self.dataproductos[i].nombre}')
            print(f'cantidad en almacen: {self.dataproductos[i].cantidad}')
            print(f'precio: {self.dataproductos[i].valor}')
            print('---------------------------\n')
        print('----------Fin de productos-----------\n')

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

    def __str__(self) -> str:
        
        return 

class Carrito:

    def __init__(self) -> None:
        self.productos = {}
 

if __name__ == '__main__':

    a = Tienda()

    a.agragar_productos('salchichon', 123, 12000)

    a.agragar_productos('salchicha', 23, 15000)

    a.imprimir_productos()

    a.modificar_precio('salchichon',11000)

    a.imprimir_productos()