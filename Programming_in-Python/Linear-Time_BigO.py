def linear_search(arr, target):
    for item in arr:
        if item == target:
            return True
    return False

# Short demo
arr = [1, 2, 3, 4, 5]
print(f"Array: {arr}")
print(f"Search for 3: {linear_search(arr, 3)}")
print(f"Search for 6: {linear_search(arr, 6)}")
print("O(n) - Linear Time")