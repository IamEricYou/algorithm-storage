import pandas as pd
import numpy as np
import csv

# Replace np.nan value with "empty" string in list.
def replace_nan_to_empty(column_list):
    return list(column_list.replace(np.nan, 'empty', regex=True))

def get_rows():
    file = pd.read_excel('template/02.99 Categorization.xlsx')
    
    prod_name_list = replace_nan_to_empty(file[1])
    prod_name_list = list(filter(('empty').__ne__, prod_name_list)) #remove empty


    file_list = file.values.T.tolist() # this can make df to list
    # file_list_remove_nan = [[i for i in x if pd.notnull(i)] for x in file_list]
    # print(file_list[4])

    # 일단 나중에 태그작업하게되면 일일히 행 번호 지정해서 하는게 제일 빠를듯 - 왜냐면 행 태그이름이 바뀔수도있으니

    # file.rows doens't work

if __name__ == "__main__":
    get_rows()