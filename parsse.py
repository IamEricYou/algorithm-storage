import csv
import pandas as pd
import numpy as np

def check_value_is_nan(val):
    if type(val) == float and np.isnan(val):
        return True
    return False

file = pd.ExcelFile('02.99 Categorization.xlsx')

recommended_itinerary_sheet_name = '추천일정_Template'
max_tag_num = sum(x.startswith('item_') for x in pd.read_excel('02.99 Categorization.xlsx', sheet_name=recommended_itinerary_sheet_name).columns.tolist()) # check how many tags in column name
rcm_itnry_sheet = file.parse(recommended_itinerary_sheet_name)

for idx, each_row in rcm_itnry_sheet.iterrows():
    how_many_days = 1

    if each_row['id'] == "ex" or check_value_is_nan(each_row['id']):
        continue

    if each_row['day_index'] == 1:
        tendency_codes = each_row['tendency_code'].split(',')
        tendency_degrees = {
            'activity': int(each_row[5]),
            "city_nature": int(each_row[6]),
            "willingness": int(each_row[7])
        }

        ri_template = {
            'title': each_row['title'],
            'status': 'DCT',
            'description': each_row['desc'],
            'tendency_codes': tendency_codes,
            'tendency_degrees': tendency_degrees,
        }

        # obj, _ = RecommendedItinerary.objects.update_or_create(
        #     id=int(each_row['id'], defaults=ri_template)
        # )

        cities_list = each_row['cities'].split(',') if not check_value_is_nan(each_row['cities']) else []
        prod_no_list = each_row['prod_no'].split(',') if not check_value_is_nan(each_row['prod_no']) else []
        rest_no_list = each_row['rest (음식점)'].split(',') if not check_value_is_nan(each_row['rest (음식점)']) else []

        