import requests
import json

# replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
url = 'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=IBM&apikey=DX774XTWD4HE3E2M'
api_response = requests.get(url)
data = api_response.text
A = json.loads(data)

print(A)
