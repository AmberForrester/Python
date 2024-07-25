import os

def findSubDirs(directory):
    sub_dirs = []
    for root, dirs, files in os.walk(directory):
        for dir_name in dirs:
            sub_dirs.append(os.path.join(root, dir_name))
    return sub_dirs

my_path = "c:/code/Python/Python-Code/"
my_sub_dirs = findSubDirs(my_path)

for my_sub_dir in my_sub_dirs:
    print(my_sub_dir)