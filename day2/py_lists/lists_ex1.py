my_list = ["It", "was", "the", "best", "of"]

my_list.append("times")
my_list.append("It")

first = my_list.pop(0)

# Sort the list, lexographically (dictionary order)
my_list.sort()

print("-" * 50)
print(my_list)
print("-" * 50)

print()
for i, val in enumerate(my_list):
    print(f"{i:>3} -> {val:>20}")
print()
