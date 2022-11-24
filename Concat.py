import pandas
import os
from os import listdir
import glob

cwd_original = os.getcwd()
path = cwd_original + '/data/2018/'
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

df2018  = pandas.concat([pandas.read_csv(f) for f in new_dir_list ])
months_order = ['2018-Jan', '2018-Feb', '2018-Mar', '2018-Apr', '2018-May', '2018-Jun', 
          '2018-Jul', '2018-Aug', '2018-Sep', '2018-Oct', '2018-Nov', '2018-Dec']
df2018.sort_values(by="Date", key=lambda column: column.map(lambda e: months_order.index(e)), inplace=True)
df2018 = df2018.loc[:, ~df2018.columns.str.contains('^Unnamed')]
path2 = cwd_original + '/final/'
df2018.to_csv(path2 + '2018.csv', index=False)

