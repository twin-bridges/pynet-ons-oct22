from rich import print

my_list = [
    ["rtr1", "rtr2", "sw1", "sw2"],
    ["22.17.1.1", "22.17.1.2", "22.17.1.20", "22.17.1.21"],
    ["sj1", "sj1", "sj1", "sj1"],
]

print("\nNested Lists:")
print(my_list)
print()

print("First List:")
print(my_list[0])
print()

print("Second List, Element 0")
print(my_list[1][0])
print()
