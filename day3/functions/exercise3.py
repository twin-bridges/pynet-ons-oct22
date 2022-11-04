def my_func(var1, var2, var3, var4):
    print()
    # f-string equals sign trick to print both variable and value
    print(f"{var1=}")
    print(f"{var2=}")
    print(f"{var3=}")
    print(f"{var4=}")
    print()


# Call using positional arguments
my_func(1, 2, 3, 4)

# Call using named arguments
my_func(var4=4, var1=1, var2=2, var3=3)

# Call with positional and named arguments
my_func(1, var3=3, var4=4, var2=2)

# Broken call - will cause an error
# my_func(var1=1, 2, 3, 4)
