import json

# Open and read the JSON file.
with open('c:/code/Python/Python-Code/day14/jobs.json', 'r') as file:
    jobs = json.load(file)
    
# Print the entire array of jobs -
print(jobs)





""" # some JSON:
x = '{ "name":"John", "age":30, "city":"New York"}'

# parse x:
y = json.loads(x)

# the result is a Python dictionary:
print(y["age"]) """
