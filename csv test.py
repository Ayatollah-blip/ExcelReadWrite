import pandas as pd
import numpy as np
from googletrans import Translator

translator = Translator()
df = pd.read_excel('C:\\Users\\acer\\Desktop\\jupiter file\\csv read and write\\test.xlsx')

selected_columns = df['mot']

array0 = selected_columns.values
array1 = []
for arr in array0:
    try:
        tr_arr = translator.translate(arr, dest= 'fr')
        array1.append(tr_arr.text)
    except Exception as e:
        print(e)
df['nom'] = array1
df.to_excel('C:\\Users\\acer\\Desktop\\jupiter file\\csv read and write\\test.xlsx', index=0)

