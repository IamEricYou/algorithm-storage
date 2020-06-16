import json

with open('tour_temp.json') as f:
    data = json.load(f)

# data_prod_desc = data.get('prod').get('description_module')
# experience_location = data_prod_desc.get('PMDL_EXPERIENCE_LOCATION')
# experience_location = experience_location.get('content').get('list')

# for item in experience_location:
#     break
#     print("EXP LO: ", item.get('latlng'))

# venue_location = data_prod_desc.get('PMDL_VENUE_LOCATION')
# location_type = venue_location.get('module_title')
# venue_location = venue_location.get('content').get('list')

# print(location_type)
# for item in venue_location:
#     break
#     print("VENUE LO: ", item.get('latlng'))

# tour_list = data_prod_desc.get('PMDL_SCHEDULE').get('content').get('properties').get('schedule_list')

# print(tour_list)

prod_desc_res = data['prod']['description_module']
schedule = prod_desc_res['PMDL_SCHEDULE']['content']['properties']
count_day = 0
seq = 0
tour_list = []
for s in schedule['schedule_list']['list']:
    count_day += 1
    seq = 0
    for each_day in s.get('daily_schedule_list').get('list'):
        seq += 1
        tour_image_url = each_day.get('media').get('media')[0].get('source_content')
        tour_template = {
            'day': count_day,
            'seq': seq,
            'desc': each_day.get('content').get('desc'),
            'image_url': tour_image_url if tour_image_url else "",
        }
        tour_list.append(tour_template)

print(tour_list)