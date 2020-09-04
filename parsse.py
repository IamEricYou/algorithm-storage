import csv
import pandas as pd
import numpy as np

# check if the value is nan
def check_value_is_nan(val):
    if type(val) == float and np.isnan(val):
        return True
    return False

import re

def cleanhtml(raw_html):
  cleanr = re.compile('<.*?>')
  cleantext = re.sub(cleanr, '', raw_html)
  return cleantext

s = '<div>만 12세 미만의 여행객은 이용 불가합니다.</div>'

print(cleanhtml(s))
