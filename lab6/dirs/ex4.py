file_path = r"lab6\dirs\tex.txt"

with open(file_path, 'a') as f:
    f.write("New line 1\n")
    f.write("New line 2\n")
    f.write("New line 3\n")

with open(file_path, 'r') as f:
    cnt = 0
    for line in f:
        cnt += 1

print("The file has {} lines.".format(cnt))
