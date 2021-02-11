import requests


def cotacao(empresa):
    response = requests.get(f'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={empresa}&apikey=HN3K887MOTQ1Z0HT')
    info = response.json()
    valor = []
    for key in info['Time Series (Daily)']:
        valor_original = info['Time Series (Daily)'][key]['4. close']
        valor_virgula = valor_original.replace('.', ',')
        valor_editado = valor_virgula[0:-2]
        valor.append(valor_editado)
    return valor


def nome(empresa):
    response = requests.get(f'https://www.alphavantage.co/query?function=SYMBOL_SEARCH&keywords={empresa}&apikey=HN3K887MOTQ1Z0HT')
    info = response.json()
    nome = info['bestMatches'][0]['2. name']
    return nome
