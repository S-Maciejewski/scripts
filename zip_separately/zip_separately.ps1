$fileExtension = "csv"

Get-ChildItem -Filter "*.$fileExtension" | ForEach-Object {
    Compress-Archive -Path $_ -DestinationPath "$($_ -replace ".$fileExtension", ".zip")"
}