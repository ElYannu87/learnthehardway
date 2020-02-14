from sys import argv
from os.path import exists

script, from_file, to_file = argv

in_file = open(from_file); indata = in_file.read()

print(f"The input file is {len(indata)} bytes long and is {exists(to_file)}")

print("Ready, hit RETURN to continue, CTRL-C to abord.")
input()

out_file = open(to_file, 'w')
out_file.write(indata)

print("Done")

out_file.close()
in_file.close()
