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

file_list = [
    'exchange_temp.json',
    'meet_temp.json',
    'pick_temp.json',
    'prod_temp.json',
    'prod_temp1.json',
    'tour_temp.json',
    'exchange_temp.json',
    'prod_temp2.json',
    'expr_temp.json'
]

with open('jsons/meeting_temp.json') as f:
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
            'image_url': replace_image_url(tour_image_url) if tour_image_url else "",
        }
        tour_list.append(tour_template)

meeting_location_lang = [
    '집합 장소', 'Meeting Point', '集合地點', '集合地點'
]

pickup_location_lang = [
    '픽업 장소', 'Pick-Up Point', '接駁地點', '接駁地點'
]
pick_meeting_location = prod_desc_res.get('PMDL_VENUE_LOCATION')
meeting_pick_lo_list = []
# pickup_lo_list = []
check_position = 0
if pick_meeting_location:
    location_type = "undefined"
    if pick_meeting_location.get('module_title') in meeting_location_lang:
        location_type = "meeting"

    if pick_meeting_location.get('module_title') in pickup_location_lang:
        location_type = "pick-up"

    for i, each_lo in enumerate(pick_meeting_location.get('content').get('list')):
        if check_position == 0 and each_lo.get('latlng').get('longitude', 0.0) != 0.0:
            #position = Point(float(each_lo.get('latlng').get('longitude', 0.0)), float(each_lo.get('latlng').get('latitude', 0.0)))
            check_position = 1

        note = []
        if location_type == 'meeting':
            if each_lo.get('arrival_desc'):
                note.append(each_lo.get('arrival_desc').get('desc'))

        if location_type == 'pick-up':
            pickup_detail_list = prod_detail_res['booking_field'].get('traffic').get('car').get('location_list').get('list_option')

            # Sometimes, the data is like 9:0, which needs to be parsed like 9:00
            parsed_s_time = pickup_detail_list[i].get('s_time').split(':')
            parsed_e_time = pickup_detail_list[i].get('e_time').split(':')

            if len(parsed_s_time[1]) != 2:
                parsed_s_time[1] += "0"

            if len(parsed_e_time[1]) != 2:
                parsed_e_time[1] += "0"

            note.append(parsed_s_time)
            note.append(parsed_e_time)

        meeting_pick_template = {
            "type": location_type,
            "name": each_lo.get('location_name').get('desc') if location_type == 'meeting' else each_lo.get('latlng').get('desc'),
            "latitude": float(each_lo.get('latlng').get('latitude', 0.0)),
            "longitude": float(each_lo.get('latlng').get('longitude', 0.0)),
            "place_id": each_lo.get('latlng').get('place_id'),
            "address": each_lo.get('latlng').get('desc') if location_type == 'meeting' else each_lo.get('location_name').get('desc'),
            "zoom": int(each_lo.get('latlng').get('zoom_lv', 0)),
            "images": replace_image_url(each_lo.get('latlng').get('map_snap_url', "")),
            "desc": note, # for pick-up, they have meeting time and depart time. The time will be saved as [meeting_time, depart_time]
            # for meeting, they may have some transportation information.
        }
        meeting_pick_lo_list.append(meeting_pick_template)

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

experience_location = prod_desc_res.get('PMDL_EXPERIENCE_LOCATION')
exp_lo_list = []
if experience_location:
    for each_exp_lo in experience_location.get('content').get('list'):
        experience_lo_template = {
            'latitude': float(each_exp_lo.get('latlng').get('latitude')),
            'longitude': float(each_exp_lo.get('latlng').get('longitude')),
            'image_url': replace_image_url(each_exp_lo.get('latlng').get('map_snap_url')),
            'zoom': int(each_exp_lo.get('latlng').get('zoom_lv')),
            'desc': each_exp_lo.get('latlng').get('desc'),
        }
        exp_lo_list.append(experience_lo_template)

print(meeting_pick_lo_list)