def my_func(x, y, z=100):
    print(f"x is {x}")
    print(f"y is {y}")
    print(f"z is {z}")
    return x + y + z


if __name__ == "__main__":
    my_list = [22, 7, 18]
    my_dict = {"x": 7, "y": 0, "z": 22}
    result = my_func(**my_dict)
    print(result)
