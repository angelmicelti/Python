# Vamos calculando los números primos y metiéndolos en una lista

limite = int(input('Dime el número máximo: '))
primos = [2]
for i in range (2, limite + 1):
    for j in primos:
        if i & j == 0:
            break
        elif( (i//j) < j):
            primos.append(i)
            break
        
print(primos)