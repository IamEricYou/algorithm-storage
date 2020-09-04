import requests 
import shutil 
import pandas as pd
import numpy as np
import csv

def check_value_is_nan(val):
    if type(val) == float and np.isnan(val):
        return True
    return False

    

f = pd.read_excel('../02.99 Categorization.xlsx', sheet_name='03. POI(TOPAS+TRAVELFLAN)')
image_col = f.columns.get_loc('image url')
name_col = f.columns.get_loc('name')

for row in f.values.tolist():
    if check_value_is_nan(row[image_col]):
        continue
    
    image_index = 0
    images = row[image_col].splitlines()
    
    for img in images:
        prefix = 'topas' if row[2] == 'TOPAS' else 'tf'
        parsed_name = ''.join(x.lower() for x in row[name_col] if not x.isspace())
        filename =  f"save/{prefix}_{row[1]}_{parsed_name}_{image_index}.jpg"
        image_index += 1
        
        r = requests.get(img, stream = True)

        if r.status_code == 200:
            r.raw.decode_content = True
            
            with open(filename,'wb') as f:
                shutil.copyfileobj(r.raw, f)
                
            print('Image sucessfully Downloaded: ',filename)
        else:
            print(row[1])
            print('Image Couldn\'t be retreived')