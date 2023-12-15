import os
import pandas as pd


txt_file_path = 'data.txt'
if os.path.exists(txt_file_path):
    with open(txt_file_path, 'r') as file:
        content = file.read()

df = pd.read_csv('data.txt', delimiter='\t')
jaut_5 = df[(df['Website'] == '.org')]
total_number = jaut_5['total_number'].sum()
print(total_number)