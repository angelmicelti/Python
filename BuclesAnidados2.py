'''Recorrer una lista de listas con dos bucles anidados'''

notas = [[6,6,7,10,9],[10,7,6,7,7],[5,5,10,7,10]]

for i in range(3):
    for j in range(5):
        if notas[i][j] == 10:
            print(i,j)