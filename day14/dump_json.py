# URL to grab data and dump it into a file. 

import requests # Install using python -m pip install requests
import json

response = requests.get('URL') # https://raw.githubusercontent.com/jamesmontemagno/app-monkeys/master/MonkeysApp/monkeydata.json

data = response.json()

with open('FILE PATH', 'w') as file:  # Example file path - ./day14/monkey.json
    json.dump(data, file)
    
print('File Created.')