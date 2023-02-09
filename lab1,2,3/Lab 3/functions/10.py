def unique_list(input_list):
    unique_elements = []
    for i in input_list: #пробегаемся по нашему изначальному списку
        if i not in unique_elements:#и при проверке задаем вопрос есть ли наш элемент в новом списке, если нет - добавляем его
            unique_elements.append(i)
    return unique_elements
list1 = [1, 2, 3, 1, 2, 5, 6, 7, 8, 6, 9, 10]
new_list = unique_list(list1)
print("Input list:", list1)
print("Output list:", new_list)