import random, math
numeroMaximo = int(input('¿Cuántos puntos quieres usar?'))

dentroCirculo = 0

for i in range(numeroMaximo):
    x = random.random() #genera un float entre 0 y 1
    y = random.random() #genera un float entre 0 y 1
    r = math.sqrt(x**2+y**2)
    if (
        r<1): #si la distancia al centro es menor que 1 el punto está dentro del círculo
        dentroCirculo +=1
        
#Como solo estamos usando un cuarto de la circunferencia, el área del círculo será pi/4 y el área del cuadrado 1. La división entre el número de puntos dentro del círculo y los totales será aproximadamente la división entrea ambas superficies. dentroCirculo/numeroMaximo = pi/4/1
resultado = 4 * dentroCirculo / numeroMaximo

print('El valor de pi es ' + str(resultado))
errorAbs = resultado - math.pi #math.pi te da el valor de pi
errorRel = abs((errorAbs / math.pi)*100)
print('El error en el cálculo de pi es del ' + str(round(errorRel, 2)) + ' por ciento')

#round redondea el valor del error relativo a dos decimales.
        