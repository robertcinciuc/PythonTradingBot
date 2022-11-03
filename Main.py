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

def realTimeAskLogic(prev, jsonResponse, cumul):
    if(prev != None):
        delta = float(jsonResponse["data"]["bestAsk"]) - float(prev["data"]["bestAsk"]);
        cumul += delta;
        print("Cumul:" + str(cumul) + "; Delta:" + str(delta));
        
        if(cumul > 2):
            print("Sell");
        
        return cumul;
    
    return 0;
    
def main():
    jsonResponseList = [];
    cumul = 0;
    prev = None;
    
    try:
        while True:
            jsonResponse = HttpRequest.addJsonResponse(jsonResponseList, 'https://api.kucoin.com/api/v1/market/orderbook/level1?symbol=BTC-USDT');
            time.sleep(0.01);
            
            if(jsonResponse != None):
                cumul = realTimeAskLogic(prev, jsonResponse, cumul);    
                prev = jsonResponse;
                
    except KeyboardInterrupt:
        print("Keyboard interrupt");
        
    # print('Prices:');    
    # for jsonResponse in jsonResponseList:
    #     print( "BestAsk:" + jsonResponse["data"]["bestAsk"] + "; BestBid:" + jsonResponse["data"]["bestBid"]);
    
    Utils.printMemoryConsumption(psutil.Process(os.getpid()));
    

if __name__ == "__main__":
    main()
