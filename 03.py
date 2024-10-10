# suma y promedio de n numeros

Nnumeros = int(input("cuantos numeros quieres sumar y promediar: "))

conteo = 0
total = 0

while conteo < Nnumeros:
    numero = int(input("ingresa un numero: "))
    total += numero
    conteo += 1
    promedio = total / Nnumeros
print(f"La suma total es: {total} y el promedio es: {promedio}")
