def display_output(msg1, msg2, msg3="Hello World"):
    print()
    print("#" * 80)
    print(f"msg1: {msg1}")
    print(f"msg2: {msg2}")
    print(f"msg3: {msg3}")
    print("#" * 80)
    print()


# Note, msg3 argument is NOT specified here
display_output(msg2="Hello", msg1="Something")
