def insertion_sort(lista):
    n = len(lista)
    for i in range(1,n):
        chave = lista[i]
        j = i - 1

        while j >=0 and lista[j] > chave:
            lista[j+1] = lista[j]
            j = j - 1

        lista[j+1] = chave


if __name__ == "__main__":
    arr = [64, 34, 25, 12, 22, 11, 90]
    
    print("Lista original:")
    print(arr)
    
    insertion_sort(arr)
    
    print("Lista ordenada usando Bubble Sort:")
    print(arr)
    