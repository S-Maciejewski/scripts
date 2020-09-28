$startedFrom = $PWD.Path

$directory = Read-Host 'Please enter a relative path to directory (leave empty for current directory)'
$recursive = Read-Host 'Please write "R" or "r" for recursive count (leave empty otherwise)'
$pattern = Read-Host 'Please enter a pattern for file names (i.e. records_*.csv)(* for all files)'

# The variables can be easily hardcoded if the script is being run automatically, as can be seen below
# $directory = './files'
# $recursive = 'r'
# $pattern = '*.txt'

Set-Location $(If ($directory) { $directory } Else { '.' })

if ($recursive -eq 'r' -or $recursive -eq 'R') {
    Get-ChildItem -Recurse $pattern | Get-Content | Measure-Object -Line | Select-Object Lines
}
else {
    Get-ChildItem $pattern | Where-Object { !$_.PSIsContainer } | Get-Content | Measure-Object -Line | Select-Object Lines
}

Set-Location $startedFrom