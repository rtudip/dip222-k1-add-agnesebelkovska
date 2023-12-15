import os
import pandas as pd


txt_file_path = 'data.txt'
if os.path.exists(txt_file_path):
    with open(txt_file_path, 'r') as file:
        content = file.read()

df = pd.read_csv('data.txt', delimiter='\t')

# 3 jautajusm        
jaut_3 = df[(df['Industry'] == 'Telecommunications') &  (df['Country'] =='Latvia')]
total_employees = jaut_3['Number of employees'].sum()
print(total_employees)