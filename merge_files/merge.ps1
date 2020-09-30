$pattern = Read-Host 'Please enter a pattern for file names (i.e. records_*.csv)(* for all files in current directory)'
# The variables can be easily hardcoded if the script is being run automatically, as can be seen below
# $pattern = '*.txt'

# Take a header from just a single file (skip the first line in all but one files)
$singleHeader = $true
$mergedFileName = 'merged.txt'


Get-ChildItem $pattern | foreach {
       $file = $_
       $fileContent = Get-Content $file  
       $toWrite = switch ($singleHeader) {
              $true { $fileContent }
              $false { $fileContent | Select -Skip 1 }
       }
       $singleHeader = $false
       Add-Content $mergedFileName $toWrite
}
Write-Output ('Results written to {0}' -f $mergedFileName)