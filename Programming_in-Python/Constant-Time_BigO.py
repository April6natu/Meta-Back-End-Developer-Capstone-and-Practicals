def access_element(arr, index):
    """ Accesses an element at a specific index in the array. """
    return arr[index]  # O(1) - Constant Time

# Demonstrate the constant time operation
print("Demonstrating O(1) - Constant Time Complexity:")
print("=" * 45)

# Create a sample array
sample_array = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

# Access elements at different indices
print(f"Array: {sample_array}")
print(f"Element at index 0: {access_element(sample_array, 0)}")
print(f"Element at index 3: {access_element(sample_array, 3)}")
print(f"Element at index 7: {access_element(sample_array, 7)}")
print(f"Element at index 9: {access_element(sample_array, 9)}")

print("\nNote: Each access takes the same amount of time regardless of index position.")
print("This is O(1) - Constant Time complexity!")