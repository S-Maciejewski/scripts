import csv
import pandas as pd  # pip install pandas
from datetime import datetime

# source file name (in case of format other than comma separated .csv, set delimiter to proper value)
file_name = 'some_file.csv'
# names of one or more columns in which date should be parsed
date_fields = ['some_column_1', 'some_column_2']
# source date format - syntax reference: https://docs.python.org/3/library/datetime.html#strftime-and-strptime-behavior
source_date_format = '%d.%m.%Y'
# desired date format, same syntax as above
destination_date_format = '%Y-%m-%d'

data = pd.read_csv(file_name, delimiter=',')  # field delimiter, ',' by default

for date_field in date_fields:
    data[date_field] = data[date_field].apply(lambda date: datetime.strptime(
        date, source_date_format).strftime(destination_date_format))

# save result to file, by default quote all fields (change to QUOTE_NONE or QUOTE_NONNUMERIC if needed)
data.to_csv(file_name.replace('.', '_parsed.'),
            index=False, quoting=csv.QUOTE_ALL)
