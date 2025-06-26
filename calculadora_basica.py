print('Bienvenido a la calculadora! Solo puedes elegir dos números.')
primer_numero = int(input('Por favor, ingresa el primer número: '))
segundo_numero = int(input('Por favor, ingresa el segundo número: '))
numero = int(input('Por favor, elige con un número la operación que deseas realizar:\n1. +, 2. -, 3. *, 4. / \n'))

if numero == 1:
    print(f'La suma de los dos números es: {primer_numero+segundo_numero}')
elif numero == 2:
    print(f'La resta de los dos números es: {primer_numero-segundo_numero}')
elif numero == 3:
    print(f'El producto de los dos números es: {primer_numero*segundo_numero}')
elif numero == 4:
    if segundo_numero != 0:
        print(f'La división de los dos números es: {primer_numero/segundo_numero}')
    else:
        print('No se puede dividir entre cero.')
else:
    print('Opción inválida. Debes elegir una operación del 1 al 4.')
