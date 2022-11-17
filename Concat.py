import pandas
import os
from os import listdir
import glob

cwd_original = os.getcwd()
path = cwd_original + '/data/2022/'
dir_list = os.listdir(path)

print(dir_list)

for file in dir_list: 
    csv = path + file
    df = pandas.read_csv(csv)
    print('Read file: ', csv)
    Date = file.replace('.csv', '')
    df['Date'] = f"{Date}"
    first_column = df.pop('Date')
    df.insert(0, 'Date', first_column)
    df.to_csv(path + file, index=False)
    print('Finished with  file: ', csv)
    
    
new_dir_list= [f"{path}" + s for s in dir_list]

df2022  = pandas.concat([pandas.read_csv(f) for f in new_dir_list ])
months_order = ['2022-Jan', '2022-Feb', '2022-Mar', '2022-Apr', '2022-May', '2022-Jun', 
          '2022-Jul', '2022-Aug', '2022-Sep', '2022-Oct', '2022-Nov', '2022-Dec']
df2022.sort_values(by="Date", key=lambda column: column.map(lambda e: months_order.index(e)), inplace=True)
df2022 = df2022.loc[:, ~df2022.columns.str.contains('^Unnamed')]
path2 = cwd_original + '/final/'
df2022.to_csv(path2 + '2022.csv', index=False)

