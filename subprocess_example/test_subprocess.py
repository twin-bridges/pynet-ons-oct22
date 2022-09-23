import subprocess

cmd_list = ["ls", "-a", "-l"]
proc = subprocess.Popen(cmd_list, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
std_out, std_err = proc.communicate()
(std_out, std_err) = [x.decode("utf-8") for x in (std_out, std_err)]

print(std_out)
print(std_err)
