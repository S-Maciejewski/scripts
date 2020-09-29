# Simple GraphQL client

This is a simple script in TypeScript working on Deno to query a GraphQL API. 
User can specify GraphQL API endpoint URL, query and optionally an API authorization token.
The result is displayed in the console and saved in a file (by default `res.json` file).

## Use
```
deno run --allow-net --allow-write .\script.ts --url 'https://api.github.com/graphql' --query '{ viewer { login } }' --key 'your github access key'
```
It is important to remember, that the `--query` argument should represent the content of the GraphQL query without the `query` keyword at the beginning, i.e.
```
{ viewer { login } }
```
instead of 
```
query { viewer { login } }
```


## Requirements
Deno 1.x

Deno installation instructions can be found at https://deno.land It can be installed with a PowerShell command on Windows
```
iwr https://deno.land/x/install/install.ps1 -useb | iex
```