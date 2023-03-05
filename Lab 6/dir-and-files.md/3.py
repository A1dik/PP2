import os

path = "/Users/user/Desktop"

if os.path.exists(path):
    print("Path exists")
    filename = os.path.basename(path)
    print("Filename:", filename)
    directory = os.path.dirname(path)
    print("Directory:", directory)
else:
    print("Path does not exist")
