import pandas
import os
import glob

cwd_original = os.getcwd()
path = cwd_original + '/final'
all_files = glob.glob(os.path.join(path, "*.csv"))

writer = pandas.ExcelWriter('Springer-Research.xlsx')

for f in all_files:
    df = pandas.read_csv(f)
    df.to_excel(writer, sheet_name=os.path.splitext(os.path.basename(f))[0], index=False)

writer.save()

