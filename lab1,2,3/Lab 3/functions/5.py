def permutations(string):
    def backtrack(first = 0):
        if first == n:
            output.append("".join(string))
        for i in range(first, n):
            string[first], string[i] = string[i], string[first]
            backtrack(first + 1)
            string[first], string[i] = string[i], string[first]
    n = len(string)
    output = []
    string = list(string)
    backtrack()
    return output

input_string = input("Enter a string: ")
result = permutations(input_string)
print("All permutations of the string are:")
for permutation in result:
    print(permutation)