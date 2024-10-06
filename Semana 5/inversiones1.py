def contar_inversiones_significativas(A, inicio, fin):
    # Caso base: Si solo hay un elemento, no hay inversiones
    if inicio == fin:
        return 0

    # Dividir el arreglo en dos mitades
    medio = (inicio + fin) // 2

    # Contar las inversiones en la primera mitad
    inversiones_izquierda = contar_inversiones_significativas(A, inicio, medio)

    # Contar las inversiones en la segunda mitad
    inversiones_derecha = contar_inversiones_significativas(A, medio + 1, fin)

    # Contar las inversiones entre las dos mitades
    inversiones_centradas = contar_y_fusionar(A, inicio, medio, fin)

    # Retornar el número total de inversiones
    return inversiones_izquierda + inversiones_derecha + inversiones_centradas

def contar_y_fusionar(A, inicio, medio, fin):
    # Contar inversiones significativas entre las dos mitades
    count = 0
    j = medio + 1

    for i in range(inicio, medio + 1):
        while j <= fin and A[i] > 2 * A[j]:
            j += 1
        count += (j - (medio + 1))  # Todos los elementos en A[medio+1..j-1] forman una inversión con A[i]

    # Ahora hacemos la fusión del arreglo para mantenerlo ordenado
    temp = []
    i, j = inicio, medio + 1

    while i <= medio and j <= fin:
        if A[i] <= A[j]:
            temp.append(A[i])
            i += 1
        else:
            temp.append(A[j])
            j += 1

    # Copiar los elementos restantes de las dos mitades
    while i <= medio:
        temp.append(A[i])
        i += 1
    while j <= fin:
        temp.append(A[j])
        j += 1

    # Copiar el subarreglo fusionado de nuevo a A
    A[inicio:fin+1] = temp

    return count

A = []
# Función principal para contar las inversiones significativas en el arreglo completo
def contar_inversiones_significativas_total(A):
    return contar_inversiones_significativas(A, 0, len(A) - 1)
