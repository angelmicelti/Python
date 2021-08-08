edad = int(input('Dime cuántos cumples este año '))
year = 2021-edad

f = open('datosAngel.txt','wt')
f.write('Ángel nació en el ' +str(year))
f.close()