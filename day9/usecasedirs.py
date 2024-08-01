import os
 
def generateTable(n):
    table = ''
    for i in range(1, 11):
        table += f"{n} X {i} = {n*i}\n"
   
    # Ensure the tables directory exists
    tables_dir = "tables"
    if not os.path.exists(tables_dir):
        print(f"Creating directory: {tables_dir}")
        os.makedirs(tables_dir)
    else:
        print(f"Directory already exists: {tables_dir}")
   
    file_path = f"{tables_dir}/table_{n}.txt"
    print(f"Writing to file: {file_path}")
    try:
        with open(file_path, "w") as f:
            f.write(table)
        print(f"Successfully wrote to file: {file_path}")
    except Exception as e:
        print(f"Error writing to file: {file_path}\n{e}")
 
for i in range(2, 21):
    generateTable(i)
    

# Code to grab files from someone elses computer using their FTP client id in line 16 of the code.     
""" file_path = f'ftp://{client_ip}/{tables_dir}/table_{n}.txt'
print(f'Writing to file: {file_path}') """