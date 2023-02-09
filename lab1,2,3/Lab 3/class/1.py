class StringOperations:
    def __init__(self):
        self.string = ""

    def get_str(self):
        self.string = input("Enter a string: ")

    def print_str(self):
        print(self.string.upper())

str_op = StringOperations()
str_op.get_str()
str_op.print_str()

