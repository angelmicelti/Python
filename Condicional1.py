print('¿Cómo te llamas?')
nombre = input()
print('¿En qué año naciste,',nombre,'?')
year=int(input())
edad = 2021-year
# print('Hola',nombre,', tienes',edad,'años')
if edad > 18:
    print('Hola',nombre,', eres muy viejo')
else:
    print('Hola',nombre,', eres muy joven')