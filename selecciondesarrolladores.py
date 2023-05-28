import sys

# leer la cantidad de competencias exigidas por la empresa
m = int(input())

# leer las competencias buscadas
competencias_buscadas = set(map(int, input().split()))

# leer la cantidad de personas que aplicaron al trabajo
n = int(input())

# contar la cantidad de personas que cumplen con las condiciones de la empresa
cumplen_condiciones = 0
for i in range(n):
    competencias_persona = set(map(int, input().split()))
    if competencias_buscadas.issubset(competencias_persona):
        cumplen_condiciones += 1

# imprimir el resultado sin espacios adicionales
sys.stdout.write(str(cumplen_condiciones))