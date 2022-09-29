def my_func(arg1, arg2, arg3):
    print(f"Hello world: {arg1} {arg2} {arg3}")


my_list = ["a", "bbb", "cccc"]
my_dict = {"arg1": "zzz", "arg2": "yyy", "arg3": "xxx"}
my_func(**my_dict)
