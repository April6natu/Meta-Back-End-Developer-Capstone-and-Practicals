my_list = [1, 2, 3]

def add_to_list(lst, item):
    nl = lst.copy()  # Create a copy of the list to avoid modifying the original
    nl.append(item)
    return nl

new_list = add_to_list(my_list, 4)

print(my_list)   # Output: [1, 2, 3]
print(new_list)  # Output: [1, 2, 3, 4