from sys import argv
# inputfile is the file you open
script, input_file = argv
# f is for file so this funtion read the file
def print_all(f):
    print(f.read())
# goes back to the beginning of the file with seek at 0
def rewind(f):
    f.seek(0)
# main function for printing out the variables and f.readline reads only the specific line
def print_a_line(line_count, f):
    print(line_count, f.readline(), end ="")
# defines the file to open via user input
current_file = open(input_file)
# just a message and due tu \n we get a line skip
print("First let's print the whole file:\n")
# calling the print all function to print the original file
print_all(current_file)

print("Now let's rewind, kind of like a tape.")
# now we seek for the beginning of the file with the ssek function
rewind(current_file)

print("Let's print three lines:")
# we define our first line we want to seek which is 1 than we call the function
# to pass our variables of current line and our file that we opened
current_line = 1
print_a_line(current_line, current_file)
# we define our first line we want to seek which is 1 and + 1 to get to line 2
# to pass our variables of current line and our file that we opened
current_line += 1
print_a_line(current_line, current_file)
# we define our first line we want to seek which is 1 + 1 again to get to line 3
# to pass our variables of current line and our file that we opened
current_line += 1
print_a_line(current_line, current_file)

current_line += 1
print_a_line(current_line, current_file)
