def inversiones_dc(A, inicio, fin):
    if inicio == fin:
        return 0 # Devuelve el pico
    medio = (fin-inicio+1) // 2

    total1= inversiones_dc(A, inicio,medio) 
    total2= inversiones_dc(A, medio+1,fin)  
    total3= Inversiones_centradas(A, inicio, medio+1,fin) 
    return total1+total2+total3

# Ejemplo de uso:
A = [1,2,3,4,5,7,8,10,12]
resultado = buscar_primero_mayor_igual(A, 0,len(A)-1)
print(f"indice pico creciente -decreciente: {resultado}")