import csv
import pandas as pd
import numpy as np

attr_data = pd.read_excel('data_summary.xlsx', sheet_name='Attr_data')

category = attr_data['구분']
city = attr_data['City']
area = attr_data['Area']
area_list = []

for cate,ci,ar, in zip(category,city,area):
    if cate == 'TravelFlan' and ci == '타이베이':
        if ar not in area_list:
            area_list.append(ar)
            
print(area_list)