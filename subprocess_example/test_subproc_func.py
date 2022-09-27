import subprocess


def subprocess_wrapper(cmd_list):
    """Wrapper to execute subprocess including byte to UTF-8 conversion."""
    proc = subprocess.Popen(cmd_list, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    std_out, std_err = proc.communicate()
    (std_out, std_err) = [x.decode("utf-8") for x in (std_out, std_err)]

    return (std_out, std_err, proc.returncode)


def output_printer(std_out, return_code):
    print()
    print(f"Return Code: {return_code}")
    print(std_out)
    print()


if __name__ == "__main__":

    cmd_list = ["ls"]
    std_out, std_err, return_code = subprocess_wrapper(cmd_list)
    output_printer(std_out, return_code)

    cmd_list = ["ls", "-a", "-l"]
    std_out, std_err, return_code = subprocess_wrapper(cmd_list)
    output_printer(std_out, return_code)
    if std_err:
        print(f"Std Err:\n{std_err}")

    cmd_list = ["find", "."]
    std_out, std_err, return_code = subprocess_wrapper(cmd_list)
    output_printer(std_out, return_code)

    cmd_list = ["find", ".", "-type", "f"]
    std_out, std_err, return_code = subprocess_wrapper(cmd_list)
    output_printer(std_out, return_code)

    cmd_list = ["find", ".", "-type", "f"]
    std_out, std_err, return_code = subprocess_wrapper(cmd_list)
    output_printer(std_out, return_code)

    cmd_list = ["./myscript.py"]
    std_out, std_err, return_code = subprocess_wrapper(cmd_list)
    output_printer(std_out, return_code)
