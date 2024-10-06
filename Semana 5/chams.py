def buscar_primero_mayor_igual(A, inicio, fin):
    if inicio == fin:
        return inicio +1 # Devuelve el pico
    medio = (inicio + fin) // 2

    if A[medio]<=A[medio +1] :
        return buscar_primero_mayor_igual(A, medio+1,fin)  # Buscar en la derecha
    else:
        return buscar_primero_mayor_igual(A,inicio, medio)  # Buscar en la izquierda

# Ejemplo de uso:
A = [1,4,7,5,3,3,2,2]
resultado = buscar_primero_mayor_igual(A, 0,len(A)-1)
print(f"indice pico creciente -decreciente: {resultado}")


def buscar_primero_mayor_igual(A, inicio, fin):
    if inicio == fin:
        return inicio +1 # Devuelve el pico 

    medio = (inicio + fin) // 2

    if A[medio]>=A[medio +1] :
        return buscar_primero_mayor_igual(A, medio+1,fin)  # Buscar en la derecha
    else:
        return buscar_primero_mayor_igual(A,inicio, medio)  # Buscar en la izquierda

# Ejemplo de uso:
A = [5,3,3,2,2,1,4,7]
resultado = buscar_primero_mayor_igual(A, 0,len(A)-1)
print(f"indice pico decreciente -creciente: {resultado}")