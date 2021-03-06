import abc

class Tienda:
    
    def __init__(self) -> None:
        self.fiadores = []
        self.dataproductos = {}
        self.carrito = Carrito()
        self.ganancias = 0
        

    def verificar_unidades(self):
        print('\n--------------Productos proximos a agotarse--------------\n')
        menores = []
        if self.dataproductos != {}:
            for i in self.dataproductos.keys():
                if self.dataproductos[i].cantidad < 5:
                    menores.append(self.dataproductos[i])
            print('\n---------------------------')
            print('   Dede de reabastecer   ')
            for i in menores:
                print('\n---------------------------')
                print(f'{i.nombre}')
            print('---------------------------\n')

    def restar_cantidades(self):
        print('\n--------------Restar o sumar Unidades a los productos--------------\n')
        try:
            nombre = str(input('Ingrese el nombre del producto al que desea cambiar unidades: '))
            cantidades_menos = int(input('Ingrese el la cantidad de unidades: '))
            print("Quieres restar o sumar cantidades?")
            opcion = int(input("Opcion:  "))
            if opcion == 1:
                if nombre in self.dataproductos.keys():
                    self.dataproductos[nombre].cantidad =- cantidades_menos
                else:
                    raise KeyError()
                if opcion == 2:
                    if nombre in self.dataproductos.keys():
                        self.dataproductos[nombre].cantidad =+ cantidades_menos
                else:
                    raise KeyError()
        except KeyError:
                print('\n---------------------------')
                print('   Producto no existente   ')
                print('---------------------------\n')

    def modificar_precio(self):
        print('\n-------------- Modificar los precios --------------\n')
        nombre = str(input('Ingrese el nombre del producto que desea eliminar: '))
        precio = int(input('Ingrese el valor nuevo del producto: '))
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

    def agregar_productos_nuevos(self):
        print('\n--------------Agregar Productos--------------\n')
        nombre = str(input('Ingrese el nombre nuevo del producto: '))
        valor = int(input('Ingrese el valor del nuevo producto: '))
        cantidad = int(input('Ingrese la cantidad del nuevo producto: '))
        if nombre in self.dataproductos.keys():
            print('\n---------------------------')
            print('   Producto ya existente   ')
            print('---------------------------\n') 
        else:
            self.dataproductos[nombre] = Productos(nombre,cantidad,valor)
            print('\n---------------------------')
            print('Producto agregado correctamente')
            print('---------------------------\n')           
    
    def eliminar_producto(self):
        print('\n-------------- Eliminar Productos --------------\n')
        nombre = str(input('ingrese el nombre del producto que desea eliminar: '))
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
        if self.dataproductos == {}:
                print('\n---------------------------')
                print(' No hay prodctos registrados ')
                print('---------------------------\n')
        else:
            for i in self.dataproductos.keys():
                print('\n---------------------------')
                print(f'nombre: {self.dataproductos[i].nombre}')
                print(f'cantidad en almacen: {self.dataproductos[i].cantidad}')
                print(f'precio: {self.dataproductos[i].valor}')
                print('---------------------------\n')
        print('----------Fin de productos-----------\n')
    
    def anadir_al_carrito(self):
        self.carrito.productos={}
        print('\n--------------A??adir Productos al Carrito--------------\n')
        while True:
            item = str(input("Ingrese el nombre del producto que quiere adquirir:  "))
            cantidad_a_adquirir = int(input("Ingrese la cantidad de unidades que desea adquirir:  "))
            if item in self.dataproductos:
                if cantidad_a_adquirir <= self.dataproductos[item].cantidad:
                    self.carrito.productos[item]= cantidad_a_adquirir
                    print(self.carrito.productos)
                    print("Desea continuar a??adiendo productos al carrito?: Responda 1 para SI, 2 para NO")
                    opcion = int(input("Opci??n:  "))
                    
            
                    if opcion == 2:
                       break

    def registrar_fiador(self, deuda = 0):
        print('\n-------------- Registar Fiadores --------------\n')
        apodo = str(input('Ingrese el nombre del nuevo fiador: '))
        celular = int(input('Ingrese el numero celular: '))
        self.fiadores.append(Fiador(apodo,celular,deuda))
        print('\n---------------------------')
        print('fiador agregado correctamente')
        print('---------------------------\n')  

    def fiar_producto(self, deuda):
        print('\n-------------- Realizar Fiados --------------\n')
        fiadores = []
        apodo = str(input('Ingrese el apodo del fiador: '))
        for i in self.fiadores:
            fiadores.append(i.apodo)
        if apodo in fiadores:
            for fiador in self.fiadores:
                if fiador.apodo == apodo:
                    fiador.deuda +=deuda
        else:
            self.registrar_fiador(deuda)
        print('\n---------------------------')
        print('fiado agregado correctamente')
        print('---------------------------\n') 

    def imprimir_fiadores(self):
        print('\n-------------- Mostrar Fiadores actuales --------------\n')
        if self.fiadores != []: 
            for fiador in self.fiadores:
                print(f'Apodo:  {fiador.apodo}')
                print(f'Deuda a la fecha:  {fiador.deuda}')        
        else:
            print('\n---------------------------')
            print(' No hay fiadores registrados ')
            print('---------------------------\n')
        print('\n----------------------------\n')
                    
    def vender_productos(self):
        print('\n-------------- Realizar Ventas --------------\n')
        valor_total= 0
        for item in self.carrito.productos.keys():
            unidades = self.carrito.productos[item]
            for i in self.dataproductos.keys():
                if item == self.dataproductos[i].nombre:
                    self.dataproductos[i].cantidad -= unidades
                    valor_total += unidades * self.dataproductos[i].valor
        print(f'El valor a pagar es:  {valor_total}')            
        while True:            
            pago = int(input("Ingrese pago dado por el cliente:  "))
            if pago < valor_total:
                print("Falta dinero, desea fiar el restante?")
                opcion = int(input("Opci??n:  "))
                if opcion == 1:
                    self.fiar_producto(valor_total-pago)
                    self.ganancias += pago
                    break
            if pago > valor_total:
                print(f'El valor a devolver es: {pago - valor_total}')
                print("GRACIAS POR SU COMPRA!")
                self.ganancias += valor_total
                break
            if pago == valor_total:
                print("GRACIAS POR SU COMPRA")
                self.ganancias += valor_total
                break

    def pagar_deuda(self):
        print('\n--------------Pagar deuda de fiados--------------\n')
        fiadores = []
        apodo = str(input("Apodo del fiador que va a pagar:  "))
        pago = int(input("Cantidad a abonar en el fiado:  "))
        for i in self.fiadores:
            fiadores.append(i.apodo)
        if apodo in fiadores:
            for fiador in self.fiadores:
                if fiador.apodo == apodo:
                    fiador.deuda -= pago
        print(f'la deuda actual es de {fiador.deuda}')
        print('\n---------------------------')
        print('abono agregado a la deuda correctamente')
        print('---------------------------\n')  

    def estadisticas_tienda(self):
        print('\n-------------- Estadisticas de la tienda --------------\n')
        deuda_total=0
        for fiador in self.fiadores:
            deuda_total += fiador.deuda
        self.imprimir_fiadores()
        print('\n----------------------------\n')
        print('\n----------------------------\n')
        print(f'La deuda total que tiene la tienda en fiados es: {deuda_total}')
        print(f'Las ganacias totales que tiene la tienda son: {self.ganancias}')
        print('\n----------------------------\n')
        print('\n----------------------------\n')
        self.verificar_unidades()


class Fiador():

    def __init__(self, apodo, celular, deuda):
        self.apodo = apodo
        self.celular = celular
        self.deuda = deuda 



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
