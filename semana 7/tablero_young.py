import numpy as np

# Tablero de Young inicial
young_tablero = np.array([[2, 3, 4,5], 
                          [ 8, 9, 12,14], 
                          [ 16, np.inf,np.inf, np.inf], 
                          [np.inf, np.inf, np.inf, np.inf]])

# Definición de la función EXTRACT_MIN
def EXTRACT_MIN(young_tablero):
    # Guardar el elemento mínimo
    min_elemento = young_tablero[0][0]
    # Colocar inf en la posición (0,0)
    young_tablero[0][0] = float('inf')
    # Reacomodar el tablero usando una rutina similar a Youngify
    YOUNGIFY(young_tablero, 0, 0)
    # Retornar el nuevo tablero y el mínimo elemento
    return min_elemento, young_tablero

# Definición de la función YOUNGIFY
def YOUNGIFY(young_tablero, i, j):
    m = len(young_tablero)
    n = len(young_tablero[0])
    
    # Coordenadas de los vecinos derecho y abajo
    down, right = (i + 1, j), (i, j + 1)
    
    # Determinar el valor más pequeño entre la posición actual, el vecino de abajo y el vecino a la derecha
    menor_i, menor_j = i, j
    
    if down[0] < m and young_tablero[down[0]][down[1]] < young_tablero[menor_i][menor_j]:
        print(1)
        menor_i, menor_j = down
    
    if right[1] < n and young_tablero[right[0]][right[1]] < young_tablero[menor_i][menor_j]:
        print(2)
        menor_i, menor_j = right
    
    # Si hay un valor más pequeño en uno de los vecinos, hacer el intercambio
    if (menor_i, menor_j) != (i, j):
        young_tablero[i][j], young_tablero[menor_i][menor_j] = young_tablero[menor_i][menor_j], young_tablero[i][j]
        # Llamada recursiva
        YOUNGIFY(young_tablero, menor_i, menor_j)

# Ejecutar la función EXTRACT_MIN con el tablero dado
min_elemento, nuevo_tablero = EXTRACT_MIN(young_tablero)

# Mostrar los resultados
print("Elemento mínimo extraído:", min_elemento)
print("Nuevo tablero de Young:")
print(nuevo_tablero)
