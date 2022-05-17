class ValorError(Exception):
  pass

while True:
    try:
        print('------------------------------')
        print('            Tienda            ')
        print('------------------------------')
        print('1.mostrar la monda')
        operacion = int(input('Ingrese el numero de la aperacion que desea realizar: '))

        if operacion == 1:
            pass
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


