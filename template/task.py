import json
import csv

with open('kr_prod.json') as f:
    data = json.load(f)


prods = data.get('prods')
number_list = []
name_list = []
url_list = []

for prod in prods:
    number_list.append(prod.get('prod_no'))
    name_list.append(prod.get('prod_name'))
    url_list.append(prod.get('prod_url_no'))

rows = zip(number_list, url_list)
with open('result.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    for row in rows:
        writer.writerow(row)

print(number_list)
print(url_list)
    