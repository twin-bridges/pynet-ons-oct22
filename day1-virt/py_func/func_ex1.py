#!/usr/bin/env python


def my_func(x, y, z=20):
    return x + y + z


print()
return_val = my_func(10, 20, 30)
print(f"Calling with three positional args: {return_val}")

return_val = my_func(x=10, y=20)
print(f"Calling with two named args: {return_val}")

return_val = my_func(10, z=13, y=20)
print(f"Calling with one positional and two named args: {return_val}")

return_val = my_func(x="x", y="y", z="z")
print(f"Calling with three strings: {return_val}")

return_val = my_func(x=["x"], y=["y"], z=["z"])
print(f"Calling with three lists: {return_val}")
print()
