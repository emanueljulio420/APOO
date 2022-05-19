import mundo

a = mundo.Tienda()

class ValorError(Exception):
  pass


while True:
    try:
        print('------------------------------')
        print('            Tienda            ')
        print('------------------------------')
        print('1.Mostrar productos')
        print('2.Agregar nuevo producto')
        print('3.Eliminar producto')
        print('4.Actualizar precio de producto')
        print('5.Mostrar estadisticas')
        print('6.Agregar producto al carrito')
        print('7.Vender productos en carrito')
        print('8.Mostarar fiadores')
        print('9.Añadir fiador')
        print('10.Ver unidades a punto de agotarse')
        print('11.restar unidades de un producto en especifico')
        print('12.Pagar deuda')
        print('13.Salir')
        operacion = int(input('Ingrese el numero de la aperacion que desea realizar: '))

        if operacion == 1:

            a.imprimir_productos()

        if operacion == 2:
            
            a.agregar_productos_nuevos()

        if operacion == 3:
            a.eliminar_producto()

        if operacion == 4:
            a.modificar_precio()

        if operacion == 5:
            a.estadisticas_tienda()

        if operacion == 6:
            a.anadir_al_carrito()

        if operacion == 7:
            a.vender_productos()

        if operacion == 8:
            a.imprimir_fiadores()

        if operacion == 9:
            a.registrar_fiador()

        if operacion == 10:
            a.verificar_unidades()

        if operacion == 11:
            a.restar_cantidades()

        if operacion == 12:
            a.pagar_deuda()

        if operacion == 13:
            print('-------- Hasta luego --------')
            break

        if 1 > operacion or operacion > 12:
            raise  ValorError()

    except ValueError:
        print('\n------------------------------')
        print('     Operacion no valida      ')
        print('------------------------------\n')
    except ValorError:
        print('\n------------------------------')
        print('     Operacion no valida      ')
        print('------------------------------\n')


