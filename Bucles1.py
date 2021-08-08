'''Programa para ver el funcionamiento de distintos bucles'''
print('Hagamos una lista de jugadores')
equipo=[] #creamos una lista vacía para poder llenarla

for i in range(5):
    print('Introduce el nombre de un jugador')
    equipo.append(input())
    
print (equipo)