# P15: Create a file and move the content from that file into another file on a different location:

# Read content in filetips.txt - 
with open('filetips.txt', 'r') as source_file:
    content = source_file.read()
    
# Append content to filehandling.txt - 
with open('filehandling.txt', 'a') as target_file:
    target_file.write(content)