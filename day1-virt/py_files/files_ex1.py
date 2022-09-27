#!/usr/bin/env python

# READ ####
f = open("myfile.txt")
my_content = f.read()
print(my_content)

# WRITE ####
print("\nWriting file.")
f = open("new_file.txt", "w")
f.write("whatever2\n")
f.close()

# APPEND ####
print("\nAppending file.")
with open("new_file.txt", "a") as f:
    f.write("something else\n")
print()
