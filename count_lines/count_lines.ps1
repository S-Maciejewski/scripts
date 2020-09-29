$startedFrom = $PWD.Path

$directory = Read-Host 'Please enter a relative path to directory (leave empty for current directory)'
$recursive = Read-Host 'Please write "R" or "r" for recursive count (leave empty otherwise)'
$pattern = Read-Host 'Please enter a pattern for file names (i.e. records_*.csv)(* for all files)'

# The variables can be easily hardcoded if the script is being run automatically, as can be seen below
# $directory = './files'
# $recursive = 'r'
# $pattern = '*.txt'

$directory = $(If ($directory) { $directory } Else { '.' })
Set-Location $directory
$size = 0

if ($recursive -eq 'r' -or $recursive -eq 'R') {
    $size = Get-ChildItem -Recurse $pattern | Measure-Object -property length -sum | Select-Object Sum
    Get-ChildItem -Recurse $pattern | Get-Content | Measure-Object -Line | Select-Object Lines, @{Name = "Size(KB)"; expression = {'{0:0.###}' -f  ($size.Sum / 1024)}}
}
else {
    $size = Get-ChildItem $pattern | Where-Object { !$_.PSIsContainer } | Measure-Object -property length -sum | Select-Object Sum
    Get-ChildItem $pattern | Where-Object { !$_.PSIsContainer } | Get-Content | Measure-Object -Line | Select-Object Lines, @{Name = "Size(KB)"; expression = {'{0:0.###}' -f  ($size.Sum / 1024)}}
}

Set-Location $startedFrom