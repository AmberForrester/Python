# P17: Delete all the files starting with a specific character or ends with a particular extension(txt, doc, etc.) - 

# For example, delete file - filetips.txt: using a full string vs. character - 

import os # Module provides functions to interact with OS, like file removal. 

import glob # Module finds all path names matching a specified pattern.

    # Defines a function delete_files that takes 2 parameters: contains_str, extension -
def delete_files(contains_str=None, extension=None):
    
    if contains_str: # Checks if string provided. 
        pattern = f"*{contains_str}*" # If provided, matches files. 
        
    elif extension: # Checks if start_str not provided but extension is
        pattern = f"*.{extension}" # Sets patter to match files ending w/ specified extension 
        
    else:
        return "Specify a string to search for or an extension." # If 2 parameters are not met, returns a message requiring one. 

    # File deletion loop - 
    for file in glob.glob(pattern): # Returns a list of files matching pattern.
        os.remove(file) # Iterates over each file that matches the pattern.
        print(f"Deleted file: {file}") # Prints the name of deleted file for confirmation.

# Will delete filetips.txt as my example - 
delete_files(contains_str='tips')  # Delete files containing 'tips'. 