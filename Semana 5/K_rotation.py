def encontrar_rotacion_recursivo(B, inicio, fin):
    # Caso base: si el subarreglo tiene un solo elemento, no hay rotación.
    if inicio == fin:
        return len(B) - (inicio)
    
    medio = (inicio + fin) // 2
    
    # Si la parte izquierda está ordenada, buscar en la parte derecha
    if B[medio] > B[fin]:
        return encontrar_rotacion_recursivo(B, medio + 1, fin)
    
    # Si la parte izquierda no está ordenada, buscar en la parte izquierda
    else:
        return encontrar_rotacion_recursivo(B, inicio, medio)

A = [1, 2, 3, 6, 7, 8, 10]
B = [3, 6, 7, 8, 10, 1, 2]
print ( "Rotacion a la derecha: ",encontrar_rotacion_recursivo(B, 0,6))

def encontrar_rotacion_recursivo(B, inicio, fin):
    # Caso base: si el subarreglo tiene un solo elemento, no hay rotación.
    if inicio == fin:
        return inicio
    
    medio = (inicio + fin) // 2
    
    # Si la parte izquierda está ordenada, buscar en la parte derecha
    if B[medio] > B[fin]:
        return encontrar_rotacion_recursivo(B, medio + 1, fin)
    
    # Si la parte izquierda no está ordenada, buscar en la parte izquierda
    else:
        return encontrar_rotacion_recursivo(B, inicio, medio)

A = [1, 2, 3, 6, 7, 8, 10]
B = [3, 6, 7, 8, 10, 1, 2]
print ( "Rotacion a la izquierda: ",encontrar_rotacion_recursivo(B, 0,6))