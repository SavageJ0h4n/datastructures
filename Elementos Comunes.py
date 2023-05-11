from queue import Queue

# Leer la entrada
lst1 = list(map(int, input().split()))
lst2 = list(map(int, input().split()))

# Crear las colas para cada lista
q1 = Queue()
q2 = Queue()

# Llenar las colas con los elementos de cada lista
for x in lst1:
    q1.put(x)

for x in lst2[::-1]:  # Recorrer la lista 2 de derecha a izquierda
    q2.put(x)

# Definir las listas resultantes
lst1_result = []
lst2_result = []

# Procesar las colas hasta que alguna se quede vacía
while not q1.empty() and not q2.empty():
    x = q1.get()
    y = q2.get()
    if x == y:
        # Si los elementos son iguales, no se añaden a las listas resultantes
        continue
    else:
        # Si los elementos son diferentes, se añaden a las listas resultantes
        lst1_result.append(x)
        lst2_result.append(y)

lst2_result.reverse()

# Imprimir los elementos resultantes de ambas listas
print((' '.join(map(str, lst1_result))), end='\n' + (' '.join(map(str, lst2_result))).strip())
