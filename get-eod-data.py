import requests

with open('sp500_tickers.txt', 'r') as f:
    sp500_tickers = f.read().split('\n')


start = 'MMM'
for ticker in sp500_tickers[sp500_tickers.index(start):]:
    print("Getting data for " + ticker)
    headers = {'Content-Type': 'text/csv', 'Accept-Encoding': None}
    resp = requests.get("https://ichart.finance.yahoo.com/table.csv?g=d&ignore=.csv&s=" + ticker, headers)
    data_lines = resp.text.split('\n')
    data_lines = [line for line in data_lines if len(line) > 0]
    for i in range(len(data_lines)):
        data_lines[i] = ticker + ',' + data_lines[i]
    data_lines[0] = data_lines[0].replace(ticker, 'symbol')
    csv = '\n'.join(data_lines)
    filename = "data/{}.csv".format(ticker)
    with open(filename, 'w') as f:
        f.write(csv)


