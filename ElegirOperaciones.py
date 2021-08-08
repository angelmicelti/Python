'''Pide dos números, y te da a elegir sumarlos, restarlos o multiplicarlos'''
print ('Dime el primer número')
a = int(input())
print ('Dime el segundo número')
b = int(input())
print ('Elige suma (s), resta(r) o multiplicación (m)')
operacion = input()
if operacion == 's':
    print('El resultado es',a+b)
elif operacion == 'r':
    print('El resultado es',a-b)
elif operacion == 'm':
    print('El resultado es',a*b)
else:
    print('No has escogido correctamente la opción')