# 5 numeros pares, impares, positivos, negativos y neutros.

conteo = 0
pares = 0
impares = 0
negativos = 0
positivos = 0
neutro = 0

while conteo < 5:
    numero = int(input("Ingresa un número: "))
    conteo += 1
    if numero == 0:
        neutro += 1
    else:
        if numero % 2 == 0:
            pares += 1
        else:
            impares += 1
        if numero > 0:
            positivos += 1
        else:
            negativos += 1

print(
    f"Tienes {pares} numeros pares, {impares} numeros impares, {positivos} positivos, {negativos} negativos y {neutro} neutro"
)
