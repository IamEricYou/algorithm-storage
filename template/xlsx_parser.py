import pandas as pd
import numpy as np
import csv

# Replace np.nan value with "empty" string in list.
def replace_nan_to_empty(column_list):
    return list(column_list.replace(np.nan, 'empty', regex=True))

def get_rows():
    file = pd.read_excel('template/02.99 Categorization.xlsx')
    print(file.columns)
    # file.rows doens't work

if __name__ == "__main__":
    get_rows()