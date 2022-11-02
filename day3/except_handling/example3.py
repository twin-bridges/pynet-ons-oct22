
my_ds = {}
my_list = []
try:
    # An error might happen here
    my_ds["invalid_key"]
    my_list[7]
except Exception:
    # An error happened - keep going.
    print("Generic exception handling")
finally:
    print("Error or no error - print this message out")
