import json

with open('prod_temp.json') as f:
    data = json.load(f)

print(data)