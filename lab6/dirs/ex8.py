import os
p=(r"lab6\dirs\goodbye.txt")
if os.path.exists(p):
    os.remove(p)
else:
    print("this file doesnt exist")