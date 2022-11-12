import json
import requests

API_URL = 'https://api.utdnebula.com'
HEADERS = {'content-type': 'application/json', 'x-api-key': 'AIzaSyAHZiXbtbX1VsJnpRrx79oADW57GY8bn2A'}

class Info:
    result = {
        'data':'',
        'error': '',
    }
    def toJSON(self)->str:
        return json.dumps(self.result)
    def Do(self):
        try:
            response = requests.get(API_URL+'/section/',headers=HEADERS)
            response.raise_for_status()
            self.result = { 'data':response.text, 'error': '' }
        except requests.exceptions.HTTPError as err:
            self.result = { 'data':'', 'error': str(err) }