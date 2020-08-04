# List all ports for UDP and listening processes

This script lists all processes listening with their process name, state and addresses / ports (both local and remote).

## Use
```
./list_processes.ps1
```
This script works best combined with 'grep' (Select-String on Windows), i.e. in order to inspect Spotify app connections one can run 
```
.\list_processes.ps1 | Select-String -Pattern "spotify"
```
The same technique can be used to find which process is listening on given port, i.e. 
```
.\list_processes.ps1 | Select-String -Pattern "LocalPort=8787"
```

## Requirements
PowerShell 5.x+ (comes as default with Windows 10) 

### Notice
This is essentially a workaround for Windows user, who can't use Linux's 
```
lsof -i -P -n
```
along with `grep`, what performs basically the same task, but unfortunately is missing in Windows. 