def find_factoral_recursive(n):
    if n == 1:
        return 1
    else:
        return n * find_factoral_recursive(n - 1)
    
print(find_factoral_recursive(5))  # Output: 120