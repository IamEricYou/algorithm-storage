import json

with open('prod_temp1.json') as f:
    data = json.load(f)

data_prod_desc = data.get('prod').get('description_module')
experience_location = data_prod_desc.get('PMDL_EXPERIENCE_LOCATION')
experience_location = experience_location.get('content').get('list')

for item in experience_location:
    print("EXP LO: ", item.get('latlng'))

venue_location = data_prod_desc.get('PMDL_VENUE_LOCATION')
location_type = venue_location.get('module_title')
venue_location = venue_location.get('content').get('list')

print(location_type)
for item in venue_location:
    print("VENUE LO: ", item.get('latlng'))
