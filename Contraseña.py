'''Te pide una contraseña en un bucle infinito hasta que la aciertas'''

password='pandereta'

while True:
    print('Escribe la contraseña')
    guess = input()
    if guess == password:
        break
    else:
        print('Ésa no es')
          
print('Estás dentro')