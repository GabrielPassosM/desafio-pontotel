import requests

def pontuacao():
    response = requests.get('https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=IBOV11.SAO&apikey=HN3K887MOTQ1Z0HT')
    info = response.json()
    valor = []
    for key in info['Time Series (Daily)']:
        valor_original = info['Time Series (Daily)'][key]['4. close']
        valor_virgula = valor_original.replace('.', ',')
        valor_editado = valor_virgula[0:-2]
        valor.append(valor_editado)
    return valor


def data():
    response = requests.get('https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=IBOV11.SAO&apikey=HN3K887MOTQ1Z0HT')
    info = response.json()
    datas = []
    for data_ori in info['Time Series (Daily)']:
        ano = data_ori[:4]
        mes = data_ori[5:7]
        dia = data_ori[-2:]
        data_edit = f'{dia}/{mes}/{ano}'
        datas.append(data_edit)
    return datas