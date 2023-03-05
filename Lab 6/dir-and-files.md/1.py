import os

path = "/Users/user/Desktop"

dirs = []
files = []

# Перебираем элементы в пути
for item in os.listdir(path):
    item_path = os.path.join(path, item)
    # проверяем дерриктория ли это, если да то закинем в деррикторию
    if os.path.isdir(item_path):
        dirs.append(item)
    # а может быть это файл и это проверим, если да то закинем в фалы
    elif os.path.isfile(item_path):
        files.append(item)

print("Directories:", dirs)
print("Files:", files)
