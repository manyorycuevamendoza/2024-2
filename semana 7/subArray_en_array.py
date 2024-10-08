import heapq

def dividir_subarrays(n, k, P, A):
    subarrays = []
    
    # Recorrer los índices de P para formar los subarrays
    for i in range(k):
        inicio = P[i] - 1  # Convertir a índices de base 0
        fin = P[i+1] - 1   # Convertir a índices de base 0
        subarrays.append(A[inicio:fin+1])  # Crear el subarray correspondiente
    print(subarrays)
    # Llamar al heap_sort_con_max_heap con los subarrays
    return heap_sort_con_max_heap(subarrays, k)

# Definición de la clase Nodo para manejar el heap
class Nodo:
    def __init__(self, key, pos):
        self.key = key  # valor del elemento
        self.pos = pos  # subarray de donde viene el elemento
    
    def __lt__(self, other):
        return self.key > other.key  # invertimos el operador para simular max-heap

# Función principal para ordenar el array usando el algoritmo dado
def heap_sort_con_max_heap(A, k):
    # Inicializar el heap y el array C para seguimiento de posiciones
    heap = []
    C = [1] * k  # Array para seguir la posición en cada subarray, inicializado en 1
    
    # Insertar el primer elemento de cada subarray en el heap
    for i in range(k):
        heapq.heappush(heap, Nodo(A[i][0], i))  # A[i][0] es el primer elemento del subarray A[i]
    
    # Array de salida B
    B = []
    
    # Extraer el máximo de cada subarray y seguir insertando hasta que el heap esté vacío
    while heap:
        # Extraer el máximo del heap
        max_nodo = heapq.heappop(heap)
        B.append(max_nodo.key)  # Añadir el valor extraído a B
        
        # Incrementar el índice del subarray correspondiente
        if C[max_nodo.pos] < len(A[max_nodo.pos]):  # Asegurarse de que no nos pasamos del subarray
            # Insertar el siguiente elemento del mismo subarray al heap
            heapq.heappush(heap, Nodo(A[max_nodo.pos][C[max_nodo.pos]], max_nodo.pos))
            C[max_nodo.pos] += 1  # Avanzar en el subarray
    
    return B

# Ejemplo de uso:
n = 9
k = 3
P = [1, 4, 7, 10]  # Indices de inicio de subarrays (P[k+1] = n+1)
A = [9, 7, 5, 8, 6, 4, 10, 3, 1]  # Array con los subarrays estrictamente decrecientes

resultado = dividir_subarrays(n, k, P, A)

print("Array ordenado en forma estrictamente decreciente:")
print(resultado)
