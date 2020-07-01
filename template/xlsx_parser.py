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
    for tag in tag_list:
        print(''.join(x.lower() for x in tag if not x.isspace()))
    print(tag_list)

# 하노키빌리지, 타이베이 101 전망대, 타이베이 101 쇼핑몰, 스무시하우스,  
def get_columns(file):
    print(file.columns)
    print(str(file.columns))
    print(file.columns.tolist())
    print(sum(x.startswith('item_') for x in file.columns.tolist()))


def get_kkday_tags(file):
    file_list = file.values.tolist()
    
    for line in file_list:
        del line[0]
        del line[0]

    print(file_list)
    return 
    for item in file_list:
        item = item[2:]
        print(item[1:])

def get_tendency_list_index(f, li):
    index_list = []
    for item in li:
        index_list.append(f.columns.get_loc(item))
    
    return index_list

def parse_tendency_question(f):
    q_code_index = f.columns.get_loc('question_code (질문 코드)')
    img_url_index = f.columns.get_loc('choice_img_url (이미지 주소)')
    choice_key_index = f.columns.get_loc('choice_key (선택지 키값)')

    file = f.values.tolist()

    tc = ['budget_01', 'travel_purpose_02']
    ic = ['landscape_03', 'activity_04', 'food_05']
    tendency_list = ['luxurious', 'lowbudget', 'active', 'static', 'city', 'nature ', 'foodtour', 'proactive', 'passive', 'food_tags']
    tendency_list_index = get_tendency_list_index(f, tendency_list)

    code_list = replace_nan_to_empty(f['question_code (질문 코드)'])
    parsed_code_list = list(set(code_list))
    parsed_code_list.remove('empty') if 'empty' in parsed_code_list else None

    for each_code in parsed_code_list:
        order_flag = 1
        each_code_list = []
        choices = []
        for each_row in file:
            # Get all rows by corresponding code
            if each_row[q_code_index] == each_code:
                each_code_list.append(each_row)
        
        for item in each_code_list:
            if each_code in tc:
                order_no = f.columns.get_loc('choice_order (선택지 순서)')
                choice_template =  {
                    "key": item[choice_key_index],
                    "text": "Empty for now",
                    "order": int(item[order_no]),
                    "tendency_points": {
                        "static": 10
                    }
                }
                # print(choice_template)
            else:
                import math
                tendency_points = {}
                extra_tags = {}
                for idx, each_idx in enumerate(tendency_list_index):
                    if type(item[each_idx]) == float and np.isnan(item[each_idx]): # if this is nan value
                        continue
                    if tendency_list[idx] == 'food_tags':
                        splitted_food_type = item[each_idx].split(',')
                        for each_food_type in splitted_food_type:
                            tendency_points.update({each_food_type:1})
                        continue
                    tendency_points.update({tendency_list[idx]: item[each_idx]}) 

                choice_template = {
                    'key': item[choice_key_index],
                    'img_url': item[img_url_index],
                    'order': order_flag,
                    'tendency_points': tendency_points
                }
                order_flag += 1
                choices.append(choice_template)


def get_tendency_tags(f):
    file = f.values.tolist()
    description_column_index = f.columns.get_loc('description')
    for each_row in file:
        v = each_row[description_column_index-4]
        if type(v) == float and np.isnan(v):
            continue
        
        print(each_row[description_column_index-4])

def get_current_data(f):
    file = f.values.tolist()
    print(f['TOPAS - TAG'][1])


# POI -> COMMON
# EXIST -> POI
# 상품 -> POI

def check_value_is_not_nan(val):
    if type(val) == float and np.isnan(val):
        return False
    return True

def parse_tags(f):
    count = 0
    for each_row in f.values.tolist():
        if check_value_is_not_nan(each_row[5]) or count == 5:
            for i in range(5,len(each_row)):
                if check_value_is_not_nan(each_row[i]):
                    # do something
                    print(each_row[i])
            break
        

def compare_tags():
    file1 = pd.read_excel('02.99 Categorization.xlsx', sheet_name='03. POI(TOPAS+TRAVELFLAN)')
    file2 = pd.read_excel('02.99 Categorization.xlsx', sheet_name='02.01 TAG-SEARCH WORD')

    poi_col = replace_nan_to_empty(file1[file1.columns[9]])
    tag_col = replace_nan_to_empty(file2[file2.columns[2]])

    for each_tag in tag_col:
        if each_tag == 'empty':
            continue
        
        if each_tag in poi_col:
            print("this goes in poi")
        else:
            print("this goes in common")

    print(tag_col)

def update_synonym():
    file = pd.read_excel('02.99 Categorization.xlsx', sheet_name='03. POI(TOPAS+TRAVELFLAN)')

    for each_row in file.values.tolist():
        print(each_row)
        
    
def update_input_entity():
    f = pd.read_excel('translation.xlsx', sheet_name='kkday_ie')

    new_header = f.iloc[0] 
    f = f[1:]
    f.columns = new_header
    file = f.values.tolist()

    id_col = f.columns.get_loc('id')
    sn_col = f.columns.get_loc('sn')
    ko_col = f.columns.get_loc('ko_KR')
    ko_extra_col = f.columns.get_loc('ko_KR__extra_info')
    print(ko_extra_col)
    return 
    for row in file:
        row_id = row[id_col]
        sn = row[sn_col]
        ko = row[ko_col]
        ko_extra = row[ko_extra_col]

def update_voucher():
    f = pd.read_excel('트래블플랜X찜카 이용권 5만원_쿠폰핀.xlsx', sheet_name='Sheet1')
    
    new_header = f.iloc[0] 
    f = f[1:]
    f.columns = new_header

    voucher_col = f.columns.get_loc('쿠폰명')
    serial_col = f.columns.get_loc('시리얼 넘버')
    product_sn = 'SE_TFP_31' # 50000
    option_sn = 'SE_TFP_31_opt1' # 50000
    is_used = False

    for row in f.values.tolist():
        print(row[serial_col])



FILE = 'translation.xlsx'
SHEET_NAME = '02.01 TAG-SEARCH WORD'
if __name__ == "__main__":
    file = pd.read_excel('02.99 Categorization.xlsx', sheet_name=SHEET_NAME)
    # file = pd.read_excel('Temporary Work.xlsx', sheet_name='성향파악_질문선택지_template')

    # file.sheet_name
    # print(file.__dict__)  

    # get_rows()
    # get_columns(file)
    # create_csv_with_tags()
    # update_tags(file)
    # get_kkday_tags(file)
    # parse_tendency_question(file)
    # get_tendency_tags(file)
    # get_current_data(file)
    # parse_tags(file)
    # compare_tags()
    # update_synonym()
    # update_input_entity()
    update_voucher()
