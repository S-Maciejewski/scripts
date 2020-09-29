import { parse } from "https://deno.land/std/flags/mod.ts"

const getApiResponse = async (endpoint: string, query: string, apiKey?: string): Promise<any> => {
    const data = await fetch(endpoint, {
        method: 'POST',
        headers: new Headers({
            'Authorization': `token ${apiKey}`,
            'Content-Type': 'application/json'
        }),
        body: JSON.stringify({ query })
    })
    return data.json()
}

const args = parse(Deno.args)

getApiResponse(args.url, args.query, args.key).then((res: any) => {
    console.log(res)
    Deno.writeTextFile('res.json', JSON.stringify(res))
})