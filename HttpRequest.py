import requests;
import json;

class HttpRequest:
    
    @staticmethod
    def addJsonResponse(jsonResponseList, url):
        response = requests.get(url);
        
        if(response.status_code == 200):
            jsonResponse = json.loads(response.text);
            jsonResponseList.append(jsonResponse);
            
        else:
            print("Error: got http code " +str(response.status_code));
            
            