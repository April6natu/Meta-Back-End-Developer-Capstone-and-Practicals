# Using explicit type conversion, change the following 
# inputs so the types match with the following below
#  
# name = type string
# age = type int
# height = type float
# loyalty = type boolean

# name = type string
name = str(input('What is your name? '))
print(f"Type of name variable is: {type(name)}. It should be <class 'str'>")

# age = type int
age = int(input('What is your age? '))
print(f"Type of age variable is: {type(age)}. It should be <class 'int'>")

# height = type float
height = float(input('What is your height in meters? '))
print(
    f"Type of height variable is: {type(height)}. It should be <class 'float'>")

# loyalty = type boolean (handle yes/no input)
loyalty_input = input(
    'Are you part of our loyalty program? (Yes/No): ').strip().lower()
loyalty = True if loyalty_input == "yes" else False
print(
    f"Type of loyalty variable is: {type(loyalty)}. It should be <class 'bool'>")
