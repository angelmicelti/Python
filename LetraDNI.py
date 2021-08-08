'''Calcula la letra del DNI usando una lista'''
letras_dni=['T','R','W','A','G','M','Y','F','P','D','X','B','N','J','Z','S','Q','V','H','L','C','K','E']
print ('Introduce tu número del DNI, si la letra')
num_dni=int(input())
resto = num_dni&23 #calcula el resto de dividir entre 23
resultado = letras_dni[resto] #escoge la letra adecuada
print('La letra de tu DNI es', resultado)