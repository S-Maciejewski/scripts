# Csv date parser
This script changes date format for given columns in .csv (or any other delimited file, .tsv etc.) and supports any format that can be described with Python's datetime syntax (docs.python.org/3/library/datetime.html).

Formatted file is saved as a new file and quoting can be specified - by default it quotes all fields with double quotes. If you just want to quote all fields (or i.e. non-numeric fields) in the file, you can specify no columns for date (leave the list empty), but this works only for files that can easily fit into memory. For bigger files consider using some other method.

This script can be used i.e. for parsing .csv files produced by Excel to formats easily readable by other software.

## Use
```
python ./main.py
```

## Requirements
python 3.x 
#### Dependencies
This script requires Pandas package, can be installed with 
```
pip instal pandas
```