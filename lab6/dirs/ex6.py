import os
for i in "abc":
    file_path = os.path.join('lab6\dirs', "{}.txt".format(i))

    if not os.path.exists(file_path):
        with open(file_path, "x"):
            pass 