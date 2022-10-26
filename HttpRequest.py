import requests;
import json;
import time;

# with open('./testImage.png', 'wb') as f:
#     f.write(response.content);

jsonResponseList = [];
for i in range(0, 10):
    response = requests.get('https://api.kucoin.com/api/v1/market/orderbook/level1?symbol=BTC-USDT');
    
    if(response.status_code == 200):
        jsonResponse = json.loads(response.text);
        jsonResponseList.append(jsonResponse);    
    
    time.sleep(0.1);
    print(i);

print('Best ask prices:');    
for jsonResponse in jsonResponseList:
    print(jsonResponse["data"]["bestAsk"]);

