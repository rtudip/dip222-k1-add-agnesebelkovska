import os
import pandas as pd


txt_file_path = 'data.txt'
if os.path.exists(txt_file_path):
    with open(txt_file_path, 'r') as file:
        content = file.read()

df = pd.read_csv('data.txt', delimiter='\t')

# 2 jautajums
def fine_employee(file_path, targeted_country):
    df = pd.read_csv(file_path)
    country = df[df['Country'] == targeted_country]
    if not country.data.empty:
        fine_employee = country['Number of employees'].sum()
        print(fine_employee) 

file_path = 'data.txt'        
targeted_country = 'Latvia'
fine_employee(file_path, targeted_country)