from requests  import *
import json

url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest'
trial_url = 'https://sandbox-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest'
# api_key = 'b54bcf4d-1bca-4e8e-9a24-22ff2c3d462c'


parameters = {
  'symbol':'ADA',
  'convert':'USD'
}

headers = {
  'Accepts': 'application/json',
  'X-CMC_PRO_API_KEY': 'b54bcf4d-1bca-4e8e-9a24-22ff2c3d462c',
}

session = Session()
session.headers.update(headers)

response = session.get(trial_url,params=parameters)
data = json.loads(response.text)
with open("data_btc.json", "w") as outfile:
    json.dump(data, outfile)

# print(type(data))
print(data['data']['ADA']['quote']['USD']['price'])
# print(data['data']{'ADA'}{'id'}{'quote'}{'usd'}{'price'})