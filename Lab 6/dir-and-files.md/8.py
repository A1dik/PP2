import os

path = "/Users/user/Desktop/sda2.txt"

if os.path.exists(path):
    if os.access(path, os.W_OK):
        os.remove(path)
        print("File deleted")
    else:
        print("File not writable, cannot delete")
else:
    print("File does not exist, cannot delete")
