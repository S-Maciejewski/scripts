# Count lines in files in a directory (or directories recursively)

This script counts lines in files matching given pattern. It outputs the number of lines, as well as total size of all files taken into account.
Lines in files can be counted both in a single dictionary and recursively in a tree of dictionaries.

## Use
```
./count_lines.ps1
```
Upon running, the user can specify:
1) the directory in which lines should be counted, 
2) whether to include files in subdirectories recursively
3) name pattern for files to count 

## Requirements
PowerShell 5.x+ (comes as default with Windows 10)

### Notice
The user input variables can be easily hardcoded into the script if necessary (i.e. for automatic running)