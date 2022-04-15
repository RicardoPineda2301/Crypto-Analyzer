## Imports
import pandas as pd
import numpy as np
#from coinmarketcapapi import CoinMarketCapAPI, CoinMrketCapAPIError
from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json

url = 'https://sandbox-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
parameters = {
  'start':'1',
  'limit':'5000',
  'convert':'USD'
}
headers = {
  'Accepts': 'application/json',
  'X-CMC_PRO_API_KEY': '6736d1a2-3230-42b1-b6d6-a4015878825d',
}

session = Session()
session.headers.update(headers)

try:
  response = session.get(url, params=parameters)
  data = json.loads(response.text)
  print(data)
  data_string = json.dumps(data)
  with open('data.json', 'w') as outfile:
    json.dump(data_string, outfile)
except (ConnectionError, Timeout, TooManyRedirects) as e:
  print(e)

