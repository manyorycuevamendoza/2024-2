
def quicksort(arr):
    comparisons = [0]  # Contador para el número de comparaciones
    swaps=[0]
    def partition(arr, low, high):
        pivot = arr[high]
        i = low - 1

        for j in range(low, high):
            comparisons[0] += 1
            if arr[j] < pivot:
                i += 1
                print("1")
                arr[i], arr[j] = arr[j], arr[i]
                swaps[0]+=1
        print("1")
        swaps[0]+=1
        arr[i+1], arr[high] = arr[high], arr[i+1]
        return i + 1

    def _quicksort(arr, low, high):
        if low < high:
            pi = partition(arr, low, high)
            _quicksort(arr, low, pi - 1)
            _quicksort(arr, pi + 1, high)

    _quicksort(arr, 0, len(arr) - 1)

    return comparisons[0], swaps[0]

# Ejemplo de uso
#arr = [1,3,2,5,6,4]# array de 6 elemetos
#arr = [1,3,2,6,5,7,4] #" array de 7 elementos"
#arr = [1,4,2,3,8,6,9,7,5] #" array de 9 elementos"
#arr= [1,3,2,5,6,7,8,9,10,11,4] 
arr = [22,24,23,32,26,27,28,29,30,31,25]
comparisons_made = quicksort(arr)
print("Número de comparaciones:", comparisons_made[0], "numeros de spwas: ",comparisons_made[1])
print("Arreglo ordenado:", arr)