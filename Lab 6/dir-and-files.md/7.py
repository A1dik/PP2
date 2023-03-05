with open("/Users/user/Desktop/sda.txt", "r") as source:
    with open("/Users/user/Desktop/sda2.txt", "w") as destination:
        destination.write(source.read())
