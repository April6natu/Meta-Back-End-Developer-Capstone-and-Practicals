def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

# Short demo
arr = [64, 34, 25, 12, 22]
print(f"Original: {arr}")
sorted_arr = bubble_sort(arr.copy())
print(f"Sorted: {sorted_arr}")
print("O(n²) - Quadratic Time")