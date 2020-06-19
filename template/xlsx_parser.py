import pandas as pd
import numpy as np
import csv

# Replace np.nan value with "empty" string in list.
def replace_nan_to_empty(column_list):
    return list(column_list.replace(np.nan, 'empty', regex=True))


TENDENCY_CODE_CHOICES = (
    'REED', 'ACE', 'ACP', 'ANE', 'ANP', 'SCE', 'SCP', 'SNE', 'SNP'
)

def get_rows():
    file = pd.read_excel('02.99 Categorization.xlsx', sheet_name='추천일정_Template')
    
    # prod_name_list = replace_nan_to_empty(file)
    # prod_name_list = list(filter(('empty').__ne__, prod_name_list)) #remove empty


    file_list = file.values.tolist() # this can make df to list
    for item in file_list:
        if item[0] == 8:
            break

        if item[1] is np.nan or item[0] == 'ex':
            continue
        title = item[1]
        description = item[3]
        tendency_codes = item[2].split(",")
        for each_code in tendency_codes:
            if each_code in TENDENCY_CODE_CHOICES:
                tendency_codes.remove(each_code)

        tendency_degrees = {
            'activity': item[5],
            "city_nature": item[6],
            "willingness": item[7]
        }
        total_days = 0

        print(tendency_codes)

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


if __name__ == "__main__":
    get_rows()
    # create_csv_with_tags()