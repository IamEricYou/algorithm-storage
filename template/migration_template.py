import json

def replace_image_url(old_url):
    parsed_url = old_url
    if "https://img.sit" in old_url or "http://img.sit" in old_url:
        parsed_url = parsed_url.replace("//img.sit","//image")

    if "/v2//image" in parsed_url:
        parsed_url = parsed_url.replace("/v2//image", "/v2/image")

    if "/v3//image" in parsed_url:
        parsed_url = parsed_url.replace("/v3//image", "/v3/image")

    return parsed_url

with open('pick_temp.json') as f:
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
        tour_image_url = ""
        if each_day.get('media'):
            tour_image_url = each_day.get('media').get('media')[0].get('source_content')
        tour_template = {
            'day': count_day,
            'seq': seq,
            'desc': each_day.get('content').get('desc'),
            'image_url': tour_image_url if tour_image_url else "",
        }
        tour_list.append(tour_template)

prod_desc_res
pick_meeting_location = prod_desc_res.get('PMDL_VENUE_LOCATION')
meeting_lo_list = []
pickup_lo_list = []

if pick_meeting_location:
    location_type = "undefined"
    if pick_meeting_location.get('module_title') == '집합 장소':
        location_type = "meeting"

    if pick_meeting_location.get('module_title') == '픽업 장소':
        location_type = "pick-up"

    for each_lo in pick_meeting_location.get('content').get('list'):
        meeting_pick_template = {
            "type": location_type,
            "name": each_lo.get('location_name').get('desc'),
            "latitude": float(each_lo.get('latlng').get('latitude')),
            "longitude": float(each_lo.get('latlng').get('longitude')),
            "place_id": each_lo.get('latlng').get('place_id'),
            "address": each_lo.get('latlng').get('desc'),
            "zoom": int(each_lo.get('latlng').get('zoom_lv')),
            "images": replace_image_url(each_lo.get('latlng').get('map_snap_url'))
        }
        meeting_lo_list.append(meeting_pick_template)

exchange_location = prod_desc_res.get('PMDL_EXCHANGE_LOCATION')
exchange_lo_list = []
if exchange_location:
    for each_lo in exchange_location.get('content').get('properties').get('locations').get('list'):
        parsed_open_days_list = []
        note_caution = each_lo.get('station_list').get('list')[0].get('arrival_desc').get('desc')
        open_days_list = each_lo.get('station_list').get('list')[0].get('active_time').get('list')
        for day in open_days_list:
            day_template = str(day.get('week_title').get('desc')) + ": " + str(day.get('start_time').get('desc')) + " - " + str(day.get('end_time').get('desc'))
            parsed_open_days_list.append(day_template)

        exchange_template = {
            'address': each_lo.get('location_info').get('properties').get('latlng').get('desc'),
            'latitude': each_lo.get('location_info').get('properties').get('latlng').get('latitude'),
            'longitude': each_lo.get('location_info').get('properties').get('latlng').get('longitude'),
            'place_id': each_lo.get('location_info').get('properties').get('latlng').get('place_id'),
            'note': str(note_caution) + ','.join(parsed_open_days_list)
        }
        exchange_lo_list.append(exchange_template)


exp_lo_list = []
if experience_location:
    for each_exp_lo in experience_location.get('content').get('list'):
        experience_lo_template = {
            'latitude': float(each_exp_lo.get('latitude')),
            'longitude': float(each_exp_lo.get('longitude')),
            'image_url': replace_image_url(each_exp_lo.get('map_snap_url')),
            'zoom': int(each_exp_lo.get('zoom_lv')),
            'desc': each_exp_lo.get('desc'),
        }
        exp_lo_list.append(experience_lo_template)

print(exchange_lo_list)