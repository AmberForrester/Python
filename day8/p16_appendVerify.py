# P16 - Append an existing file and verify the content in it: 

# Read the content from filetips.txt
with open('filetips.txt', 'r') as source_file:
    content = source_file.read()
    
# Append the content of filetips.txt to filehandling.txt, including a message - 
with open('filehandling.txt', 'a') as target_file:
    target_file.write(content)
    target_file.write('\nContent was moved from filetips.txt\n')

# Verify the content in filetips.txt by printing it - 
print("Content of filetips.txt:")
print(content)