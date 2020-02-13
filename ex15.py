# import sys
# from sys import argv
# naming script
# script, filename = argv
# open the file
filename = input("Filename?")
txt = open(filename, 'w')
line4 = input("Line4: ")

# print and read file
print(f"Here's your file {filename}")
txt.write(line4)
txt.write("\n")
txt.close()
