import wolframalpha

client = wolframalpha.Client('AT7WGY-VYHTRXUJK7')

while True:
    queryText = str(input('Query: '))
    res = client.query(queryText)
    output = next(res.results).text
    print(output)
