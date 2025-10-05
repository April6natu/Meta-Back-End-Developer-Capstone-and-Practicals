def read_file(file_name):
    """ Reads and returns the entire contents of a file as a single string. """
    with open(file_name, "r") as f:
        contents = f.read()
    print(contents)
    return contents


def read_file_into_list(file_name):
    """ Reads a file and returns a list where each element is a line in the file. """
    with open(file_name, "r") as f:
        lines = f.readlines()   # keeps '\n'
    return lines


def write_first_line_to_file(file_contents, output_filename):
    """ Writes the first line of a given string to an output file. """
    first_line = file_contents.split("\n")[0]
    with open(output_filename, "w") as f:
        f.write(first_line)


def read_even_numbered_lines(file_name):
    """ Reads even-numbered lines of a file and returns them as a list. """
    even_lines = []
    with open(file_name, "r") as f:
        for idx, line in enumerate(f, start=1):
            if idx % 2 == 0:  # even-numbered line
                even_lines.append(line)   # keep newline
    return even_lines


def read_file_in_reverse(file_name):
    """ Reads a file and returns a list of its lines in reverse order. """
    with open(file_name, "r") as f:
        lines = f.readlines()
    reversed_lines = lines[::-1]  # keep newlines
    print(reversed_lines)
    return reversed_lines


# Call the functions to demonstrate their functionality
if __name__ == "__main__":
    print("Reading entire file:")
    read_file("sampletext.txt")
    
    print("\nReading file into list:")
    lines = read_file_into_list("sampletext.txt")
    print(lines)
    
    print("\nWriting first line to output file...")
    with open("sampletext.txt", "r") as f:
        content = f.read()
    write_first_line_to_file(content, "first_line.txt")
    print("First line written to 'first_line.txt'")
    
    print("\nReading even-numbered lines:")
    even_lines = read_even_numbered_lines("sampletext.txt")
    print(even_lines)
    
    print("\nReading file in reverse:")
    read_file_in_reverse("sampletext.txt")
