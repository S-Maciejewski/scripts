# Merge multiple files

This script performs a simple task of merging multiple files together. 
User specifies a name pattern and the script merges all the files in current directory into a single one (skipping headers in all but one file by default). By default it produces `merged.txt` file, but it can be easily changed.

Used mostly in aggregating data from several .csv files into a single one.

## Use
```
./merge.ps1
```
Upon running, the user can specify name pattern for files to count. 

## Requirements
PowerShell 5.x+ (comes as default with Windows 10)

### Notice
The user input variables can be easily hardcoded into the script if necessary (i.e. for automatic running)