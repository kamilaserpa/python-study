def bubble_sort(arr):
    n = len(arr)
    for i in range(n - 1): # python desconsidera o ultimo item, assim n = 7, n-1=6, e o range vai de 0 - 5
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                # Trocar os elementos
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

if __name__ == "__main__":
    arr = [64, 34, 25, 12, 22, 11, 90]
    
    print("Lista original:")
    print(arr)
    
    bubble_sort(arr)
    
    print("Lista ordenada usando Bubble Sort:")
    print(arr)
    