
my_ds = {}
try:
    # An error might happen here
    my_ds["invalid_key"]
except KeyError:
    # The specified error happened - what do I do about it.
    print("Handling KeyError exception")

my_list = []
try:
    # Another error might happen
    my_list[7]
except IndexError:
    # The error happened - handle it
    print("The given list index didn't exit")