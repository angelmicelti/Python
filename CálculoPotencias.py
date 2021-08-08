'''Calcula potencias'''
print('Escribe la base')
base = int(input())
print('Escribe el exponente')
exponente = int(input())

acumulado = base

for i in range(exponente-1):
    acumulado=acumulado*base
    
print('El resultado es', acumulado)