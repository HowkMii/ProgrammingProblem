
n = int(input())
arr = list(map(int, input().split()))

ans, cnt = [], 0

branch = "Neesham"

# Quick Sort
def quickSort(arr, n):
    
        if len(arr) <= 1:
            return 0
    
        pivot = arr[0]
        l, r = [], []
    
        for i in range(1, n):
    
            if arr[i] <= pivot:
                l.append(arr[i])
    
            else:
                r.append(arr[i])
    
        quickSort(l, len(l))
        quickSort(r, len(r))
    
        arr[:] = l + [pivot] + r
    
        return arr;

# Bubble Sort
def bubbleSort(arr, n):

    for i in range(n):
        # n - i - 1
        for j in range(0, n - i - 1):

            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    return arr;

# Selection Sort
def selectionSort(arr, n):

    for i in range(n):

        m_ele = arr[i]
        m_ind = i 

        for j in range(i + 1, n):

            if arr[j] < m_ele:
                m_ele = arr[j]
                m_ind = j 

        arr[i], arr[m_ind] = arr[m_ind], arr[i]

    return arr;

# Insertion Sort
def insertionSort(arr, n):

    for i in range(1, n):
        
        j = i - 1
        key = arr[i]

        while (j >= 0 and key < arr[j]):

            arr[j + 1] = arr[j]
            j -= 1

        j += 1
        arr[j] = key

    return arr;

# Merge Sort
def mergeSort(arr, n):
    
    if len(arr) <= 1:
        return 0

    mid = n // 2 

    l = arr[:mid]
    r = arr[mid:]

    mergeSort(l, len(l))
    mergeSort(r, len(r))

    i, j, k = 0, 0, 0 

    while (i < len(l) and j < len(r)):

        if l[i] <= r[j]:
            arr[k] = l[i]
            i += 1 

        else:
            arr[k] = r[j]
            j += 1

        k += 1

    while (i < len(l)):
        arr[k] = l[i]
        k += 1 
        i += 1

    while (j < len(r)):
        arr[k] = r[j]
        k += 1
        j += 1

    return arr;

arr = insertionSort(arr, n)
print(arr)