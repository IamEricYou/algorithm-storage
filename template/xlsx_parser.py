import pandas as pd
import numpy as np
import csv

# Replace np.nan value with "empty" string in list.
def replace_nan_to_empty(column_list):
    return list(column_list.replace(np.nan, 'empty', regex=True))

CITY_NAME_KR_TO_EN = {
    '타이베이': 'Taipei',
    '타이중': 'Taichung',
    '가오슝': 'Kaohsiung',
    '타이난': 'Tainan',
    '화련': 'Hualien',
    '미아오리': 'Miaoli',
    '신베이시': 'New Taipei',
    '이란': 'Yilan',
    '펑후': 'Penghu',
    '컨딩': 'Kenting'
}

TENDENCY_CODES = (
    'REED', 'ACE', 'ACP', 'ANE', 'ANP', 'SCE', 'SCP', 'SNE', 'SNP'
)

def get_poi_id_from_item(item):
    vendor_id, vendor_uid = item.split('_')[0], item.split('_')[1]
    print(vendor_id, vendor_uid)

def get_rows():
    file = pd.read_excel('02.99 Categorization.xlsx', sheet_name='추천일정_Template')
    
    # prod_name_list = replace_nan_to_empty(file)
    # prod_name_list = list(filter(('empty').__ne__, prod_name_list)) #remove empty


    file_list = file.values.tolist() # this can make df to list
    for item in file_list:
        # if item[0] == 8:
        #     break

        # if item[1] is np.nan or item[0] == 'ex':
        #     continue
        # title = item[1]
        # description = item[3]
        # cities_list = item[4].split(",")
        # tendency_codes = item[2].split(",")
        # for each_code in tendency_codes:
        #     if each_code in TENDENCY_CODES:
        #         tendency_codes.remove(each_code)

        # tendency_degrees = {
        #     'activity': item[5],
        #     "city_nature": item[6],
        #     "willingness": item[7]
        # }
        # total_days = 0

        # for each_city in cities_list:
        #     city_name_en = CITY_NAME_KR_TO_EN.get(each_city)
        #     if not city_name_en:
        #         print("Poi city " + str(city_name_en) + " doens't exist", each_city)
        #         continue

        # get_poi_id_from_item('tf_78123')
        day_index = 1
        description = item[3]
        if item[0] == 4:
            break
        item_count = 0
        for idx in range(12, 50):
            if item[idx] is np.nan:
                break
            item_count += 1
        for i in range(12, 12+item_count):
            print(int(item[10]), item[11], item[i])

        # print(tendency_codes)

    # print(file_list[2])
    # file_list_remove_nan = [[i for i in x if pd.notnull(i)] for x in file_list]
    # print(file_list[4])

    # 일단 나중에 태그작업하게되면 일일히 행 번호 지정해서 하는게 제일 빠를듯 - 왜냐면 행 태그이름이 바뀔수도있으니

    # file.rows doens't work

def create_csv_with_tags():
    tags = ['num', 'str']
    temp_a = [1,2,3,4,5]
    temp_b = ['a','b','c','d','e']

    with open('hello.txt', 'w') as f:
        file = csv.writer(f, delimiter=',')
        file.writerow(tags)
        file.writerow(temp_a)
        file.writerow(temp_b)

def validate_tags(tag_name):
    if 'ps_' in tag_name:
        return False

    if 'PS_' in tag_name:
        return False

    if 'ts_' in tag_name:
        return False

    if 'tf_' in tag_name:
        return False

    if 'r_' in tag_name:
        return False

    if 'empty' in tag_name:
        return False

    if tag_name == '태그이름(exist poi가 아닐때는 태그 이름으로)':
        return  False

    return True

def update_tags(file):

    tag_list = []
    for item in file:
        if item.startswith('item_'):
            tag_column = replace_nan_to_empty(file[item])
            for each_tag in tag_column:
                tag_list.append(each_tag) if validate_tags(each_tag) else None
    
    # Some tags, which are same but have different space in the word, are manually removed
    tag_list = list(set(tag_list))
    tag_list.remove('타이베이101 전망대')
    tag_list.remove('타이베이101쇼핑몰')
    for tag in tag_list:
        print(''.join(x.lower() for x in tag if not x.isspace()))
    print(tag_list)

def get_columns(file):
    print()

if __name__ == "__main__":
    file = pd.read_excel('02.99 Categorization.xlsx', sheet_name='추천일정_Template')
    # get_rows()
    get_columns(file)
    # create_csv_with_tags()
    # update_tags(file)
