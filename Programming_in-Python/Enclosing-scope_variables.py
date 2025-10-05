def get_total(a, b):
    #enclosed variable declared inside a function
    total = a + b

    def double_it():
        #local variable
        double = total * 2
        print(f"Double the total: {double}")
        return double

    result = double_it()
    #double variable will not be accessible outside double_it()
    # print(double)  # This would cause an error
    print(f"Total: {total}")
    
    # To demonstrate the scope issue, let's use try-except:
    try:
        print(double)
    except NameError as e:
        print(f"Error: {e}")
        print("The variable 'double' is only accessible within the double_it() function")

    return total

# Call the function to see output
print("Demonstrating enclosing scope:")
final_total = get_total(5, 3)
print(f"Final total returned: {final_total}")