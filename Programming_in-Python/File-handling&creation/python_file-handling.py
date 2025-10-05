# Better approach using 'with' statement for automatic file closing
try:
    with open('test.txt', mode='r') as file:
        data = file.readline()
        print("Data read from file:")
        print(data)
        
        # Optional: read all lines if you want to see the entire file
        file.seek(0)  # Go back to the beginning
        all_data = file.read()
        print("\nAll file content:")
        print(repr(all_data))  # repr() shows special characters like \n
        
except FileNotFoundError:
    print("Error: The file 'test.txt' was not found.")
except IOError:
    print("Error: Could not read the file.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")

print("\nFile handling completed successfully!")