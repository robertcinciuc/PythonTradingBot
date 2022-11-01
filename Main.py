import json;
import os, sys;
import time;

# Importing psutil
sys.stderr = open(os.devnull, "w");
try:
    import psutil;
except:
    print("Actual psutil modules not found");
finally:
    sys.stderr = sys.__stderr__

# Local imports
from Utils import Utils;
from HttpRequest import HttpRequest;

def logicAsk(jsonResponseList):
    cumul = 0;
    for i in range(0, len(jsonResponseList)):
        if(i > 0):
            delta = float(jsonResponseList[i]["data"]["bestAsk"]) - float(jsonResponseList[i-1]["data"]["bestAsk"]);
            print(delta);
            cumul += delta;
    
    print("Cumul:" + str(cumul));
    
    
def main():
    jsonResponseList = [];
    for i in range(0, 10):
        HttpRequest.addJsonResponse(jsonResponseList, 'https://api.kucoin.com/api/v1/market/orderbook/level1?symbol=BTC-USDT');
        
        time.sleep(0.1);
        print(i);
    
    print('Prices:');    
    for jsonResponse in jsonResponseList:
        print( "BestAsk:" + jsonResponse["data"]["bestAsk"] + "; BestBid:" + jsonResponse["data"]["bestBid"]);
    
    Utils.printMemoryConsumption(psutil.Process(os.getpid()));
    
    logicAsk(jsonResponseList);

if __name__ == "__main__":
    main()
