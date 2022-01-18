from requests import *
# from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json

cmc_api_key = '2fb74590-7a69-4d74-823d-a1f4e495b147'
cmc_api_server = 'sandbox-api.coinmarketcap.com'

# sandbox-api.coinmarketcap.com
# b54bcf4d-1bca-4e8e-9a24-22ff2c3d462c
url = 'https://sandbox-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
parameters = {
  'start':'1',
  'limit':'5000',
  'convert':'USD'
}
headers = {
  'Accepts': 'application/json',
  'X-CMC_PRO_API_KEY': 'b54bcf4d-1bca-4e8e-9a24-22ff2c3d462c',
}

session = Session()
session.headers.update(headers)

try:
  response = session.get(url, params=parameters)
  data = json.loads(response.text)

  print(data)
except (ConnectionError, Timeout, TooManyRedirects) as e:
  print(e)