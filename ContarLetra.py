'''Cuenta las letras "a" que hay en una palabra'''
print('Escribe una palabra en minúsculas y sin tildes')
palabra = input()

acumulado = 0

for i in palabra:
    if i =='a':
        acumulado=acumulado+1
        
print('El número de aes es', acumulado)