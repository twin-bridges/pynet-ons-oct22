"""
a. Create a python script with three strings representing three names
b. Print these three names out in a column 30 wide, right aligned
c. Execute the script verify the output
d. Add a prompt for a fourth name, print this out as well
e. Check your code into Git and GitHub
"""

name1 = "jon"
name2 = "richard"
name3 = "joe"
name4 = input("\nEnter fourth name: ")

print(f"{name1:>30}")
print(f"{name2:>30}")
print(f"{name3:>30}")
print(f"{name4:>30}")
