my_list = ["apple", "banana", "cherry"]

with open("/Users/user/Desktop/sda.txt", "w") as file:
    for item in my_list:
        file.write("%s\n" % item)
