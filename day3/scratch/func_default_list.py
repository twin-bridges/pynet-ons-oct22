# Do NOT do this!
def display_output(var1, var2, var3=[]):
    print("Hello")


# Instead, do this
def display_output(var1, var2, var3=None):
    if var3 is None:
        var3 = []
    print("Hello")
