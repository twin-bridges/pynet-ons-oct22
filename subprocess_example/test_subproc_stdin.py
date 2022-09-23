import subprocess

cmd_list = ["./myscript.py"]
stdin_responses = "8.8.8.8\n"
proc = subprocess.Popen(
    cmd_list,
    stdout=subprocess.PIPE,
    stdin=subprocess.PIPE,
    stderr=subprocess.PIPE,
    bufsize=1,  # Use line-buffering (send line when a newline is encountered)
    universal_newlines=True,  # Input/output gets converted to/from text
)
std_out, std_err = proc.communicate(input=stdin_responses)

print()
print(std_out)
print()
