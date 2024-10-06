def buscar_primero_mayor_igual(A, m, inicio, fin):
    if inicio == fin:
        return len(A)-inicio  # Devuelve el índice donde los elementos comienzan a ser mayores o iguales

    medio = (inicio + fin) // 2

    if m >A[medio]:
        return buscar_primero_mayor_igual(A, m, medio +1,fin)  # Buscar en la izquierda
    else:
        return buscar_primero_mayor_igual(A, m, inicio, medio)  # Buscar en la derecha

# Ejemplo de uso:
A = [1, 2, 3, 4, 7, 8, 10, 12]
m = 9
resultado = buscar_primero_mayor_igual(A, m,0,len(A)-1)
print(f"La cantidad de elementos mayores o iguales a {m} es: {resultado}")

def buscar_primero_mayor_igual(A, m, inicio, fin):
    if inicio == fin:
        return inicio  # Devuelve el índice donde los elementos comienzan a ser mayores o iguales

    medio = (inicio + fin) // 2

    if m > A[medio]:
        return buscar_primero_mayor_igual(A, m, medio +1,fin)  # Buscar en la izquierda
    else:
        return buscar_primero_mayor_igual(A, m, inicio, medio)  # Buscar en la derecha

# Ejemplo de uso:
A = [1, 2, 3, 4, 7, 8, 10, 12]
m = 9
resultado = buscar_primero_mayor_igual(A, m,0,len(A)-1)
print(f"La cantidad de elementos mayores o iguales a {m} es: {resultado}")

