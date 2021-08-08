'''Pide al usuario que adivine un número usando un while'''

clave = 2
prueba = 0 #por si hay en la memoria algún valor de una ejecución anterior del programa, inicializamos a cero.
print('¡Empezamos!')

while prueba != clave:
    print('Adivina un número entre 0 y 10')
    prueba = int(input())
    
print('¡Acertaste!')