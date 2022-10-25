import requests;
import json;

response = requests.get('https://api.kucoin.com/api/v1/market/orderbook/level1?symbol=BTC-USDT');
# curl -s https://api.kucoin.com/api/v1/market/orderbook/level1?symbol=BTC-USDT

# with open('./testImage.png', 'wb') as f:
#     f.write(response.content);

# print(response.text);

jsonResponse = json.loads(response.text);
print(jsonResponse["data"]["bestAsk"]);
print(jsonResponse);

