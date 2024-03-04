import os

file1 = r"lab6\dirs\fromhere.txt"
file2 = r"lab6\dirs\tohere.txt"

with open(file1, "r") as f1, open(file2, "w") as f2:
        for line in f1:
            f2.write(line)