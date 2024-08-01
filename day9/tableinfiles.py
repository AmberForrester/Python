""" import os # Module provides a way of using OS to create directories, removing files.  """

def generateTable(n):
    table = ''
    for i in range(1, 11):
        table += f'{n} x {i} = {n*i}\n'
        
    """ # Ensure the 'day9/tables' directory exists
    os.makedirs('day9/tables', exist_ok=True) """
    
    f = open(f'tables/table_{n}.txt', 'w')
    f.write(table)
        
for i in range(2, 21):
    generateTable(i)