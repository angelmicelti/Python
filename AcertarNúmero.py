'''Adivina un número entre 1, 2 y 3
El número a adivinar es el 2'''
print ('Dime un número entre el 1 y el 3')
test = input()
if test == '1' or test == '3':
    print ('Has fallado')
elif test == '2':
    print ('Has acertado')
else:
    print ('No has escrito un número entre el 1 y el 3')