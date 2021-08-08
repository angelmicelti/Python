'''Calcula potencias'''
print('Escribe la base')
base = int(input())
print('Escribe el exponente')
exponente = int(input())

acumulado = 1
for i in range(exponente):
    acumulado = acumulado*base
    
print('El resultado es', acumulado)