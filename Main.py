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

def main():
    jsonResponseList = [];
    for i in range(0, 10):
        HttpRequest.addJsonResponse(jsonResponseList, 'https://api.kucoin.com/api/v1/market/orderbook/level1?symbol=BTC-USDT');
        
        time.sleep(0.1);
        print(i);
    
    print('Best ask prices:');    
    for jsonResponse in jsonResponseList:
        print(jsonResponse["data"]["bestAsk"]);
    
    Utils.printMemoryConsumption(psutil.Process(os.getpid()));


if __name__ == "__main__":
    main()
