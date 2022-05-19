
class ValorError(Exception):
  pass


while True:
    try:
        print('------------------------------')
        print('            Tienda            ')
        print('------------------------------')
        print('1.Mostrar productos')
        print('2.Agregar nuevo producto')
        print('3.Eliminar product')
        print('4.Actualizar precio de producto')
        print('5.Mostrar productos')
        print('6.Mostrar productos')
        operacion = int(input('Ingrese el numero de la aperacion que desea realizar: '))

        if operacion == 1:
            if tienda.dataproductos == {}:
                print('\n---------------------------')
                print(' No hay prodctos registrados ')
                print('---------------------------\n')
            else:
                tienda.imprimir_productos()

        if operacion == 2:
            pass

        if operacion == 3:
            pass

        if operacion == 4:
            pass

        if operacion == 5:
            pass

        if operacion == 6:
            pass

        if operacion == 7:
            pass

        if operacion == 8:
            pass

        if operacion == 9:
            pass

        if operacion == 10:
            pass

        if 1 > operacion or operacion > 10:
            raise  ValorError()

    except ValueError:
        print('\n------------------------------')
        print('     Operacion no valida      ')
        print('------------------------------\n')
    except ValorError:
        print('\n------------------------------')
        print('     Operacion no valida      ')
        print('------------------------------\n')


