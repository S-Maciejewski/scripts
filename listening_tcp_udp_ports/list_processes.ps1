get-nettcpconnection | Select-Object local*, remote*, state, @{Name = "ProcessName"; Expression = { (Get-Process -Id $_.OwningProcess).ProcessName } }
