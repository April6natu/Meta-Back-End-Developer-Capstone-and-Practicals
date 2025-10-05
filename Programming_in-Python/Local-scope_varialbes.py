def get_total(a, b):
    #local variable declared inside a function
    total = a + b
    return total

print(get_total(5, 2))  # This will print: 7

# Accessing variable outside of the function:
# print(total)  # This would cause: NameError: name 'total' is not defined

# To demonstrate the error, let's use a try-except block:
try:
    print(total)
except NameError as e:
    print(f"Error: {e}")
    print("The variable 'total' is only accessible within the get_total() function")