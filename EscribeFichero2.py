f = open('secuenciaNum.txt', 'at')

while True:
    num = input('Escribe un número y pulsa intro. Pulsa sólo intro para terminar.')
    if num =='':
        break
    else:
        f.write(num + ' ')
        
f.close()