# P1: Pick up the directory and subdirectories from a given path, using the `os` module - 

"""
import os 

my_path = 'c:/code/Python/Python-Code/'
folderContents = os.listdir(my_path)

print(folderContents)

"""

import os 

my_path = 'c:/code/Python/Python-Code/'

# Using the os.walk() function will get a more detailed view that includes both directories and subdirectories -> generating the file names in a directory tree either top-down or bottom-up - 

for dirpath, dirnames, filenames in os.walk(my_path):
    print(f'Directory: {dirpath}') # A string, the path to the directory
    print('Subdirectories:', dirnames) # A list of the names of the subdirectories in the `dirpath`
    print('Files:', filenames) # A list of the names of the non-directory files in `dirpath`
    print('-' * 40)


