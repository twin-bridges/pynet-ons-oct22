import os

import pdbr

pdbr.set_trace()
print()
print("Current working directory")
start_dir = os.getcwd()
print(os.getcwd())

print()
print("Path of module we are executing")
print(os.path.realpath(__file__))

print()
print("Is this a file?")
print(os.path.isfile(__file__))

print()
print("Change directory into /tmp")
os.chdir("/tmp")
print(os.getcwd())

print()
print("Change directory back")
os.chdir(start_dir)
print(os.getcwd())

print()
print("Interface to system: simple")
os.system("ping 8.8.8.8 -c 4")
