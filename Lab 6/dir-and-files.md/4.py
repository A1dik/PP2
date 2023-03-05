with open("/Users/user/Desktop/sda.txt") as file:
    line_count = sum(1 for line in file)
    print("Number of lines in file:", line_count)
