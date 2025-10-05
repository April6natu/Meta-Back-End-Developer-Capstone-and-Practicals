with open('newfile.txt', 'w') as file:
    file.writelines(["This is a new file created!", "\nThis is another line to be added."])

# Read and display the content
with open('newfile.txt', 'r') as file:
    content = file.read()
    print(content)