from requests  import *
import json

trial_url = 'https://sandbox-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest'
trial_api_key = 'b54bcf4d-1bca-4e8e-9a24-22ff2c3d462c'

url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest'
api_key = '2fb74590-7a69-4d74-823d-a1f4e495b147'
def price(symbol):
    parameters = {
        'symbol': symbol,
        'convert': 'USD'
    }

    headers = {
        'Accepts': 'application/json',
        'X-CMC_PRO_API_KEY': api_key,
    }

    session = Session()
    session.headers.update(headers)

    response = session.get(url, params=parameters)
    data = json.loads(response.text)
    with open("data_btc.json", "w") as outfile:
        json.dump(data, outfile)

    # print(type(data))
    var = data['data'][symbol]['quote']['USD']['price']
    round(var, 2)
    message=(f"The current price of {symbol} is {var}.")
    return var

def supply(symbol):
    parameters = {
        'symbol': symbol,
        'convert': 'USD'
    }

    headers = {
        'Accepts': 'application/json',
        'X-CMC_PRO_API_KEY': api_key,
    }

    session = Session()
    session.headers.update(headers)

    response = session.get(url, params=parameters)
    data = json.loads(response.text)
    with open("data_btc.json", "w") as outfile:
        json.dump(data, outfile)

    # print(type(data))
    max_supply = data['data'][symbol]['max_supply']
    circulating_supply = data['data'][symbol]['circulating_supply']
    total_supply = data['data'][symbol]['total_supply']

    message = ""
    if max_supply != None:
        round(max_supply, 2)
        message = message+(f'\nThe maximum supply of {symbol} is {"{:,.2f}".format(max_supply)}.\n')
    if circulating_supply != None:
        round(circulating_supply, 2)
        message = message + (f'Current Circulating supply of {symbol} is {"{:,.2f}".format(circulating_supply)}.\n')
    if total_supply != None:
        round(total_supply, 2)
        message = message + (f'Total supply of {symbol} is {"{:,.2f}".format(total_supply)}.\n')
    return message