def spy_game(nums):
    code = [0, 0, 7, 'x']
    for num in nums:
        if num == code[0]:
            code.pop(0)
    return len(code) == 1
n = [1,2,3,4,5,6,0,0,2,2,3,4,]
print(spy_game(n))