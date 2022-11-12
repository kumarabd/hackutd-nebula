import json
import requests
import os
import models

API_URL = 'https://api.utdnebula.com'
HEADERS = {'content-type': 'application/json', 'x-api-key': os.environ['API_KEY']}

# Store
professor_objs = []

def remove_v(dct):
    if '__v' in dct:
        dct.pop('__v', None)
    if 'office_hours' in dct:
        print(dct['office_hours'])
    return dct 

class Info:
    def get_courses(self):
        try:
            response = requests.get(API_URL+'/course/',headers=HEADERS)
            response.raise_for_status()
            return models.Result(response.text, '')
        except requests.exceptions.HTTPError as err:
            return models.Result('', str(err))
        
    def get_professors(self):
        try:
            response = requests.get(API_URL+'/professor/',headers=HEADERS)
            response.raise_for_status()
            j = json.loads(response.text,object_hook=remove_v)
            professor_objs = []
            for mem in j['data']:
                professor_objs.append(models.Professor(**mem))
            return models.Result(professor_objs, '')
        except requests.exceptions.HTTPError as err:
            return models.Result('', str(err))
    
    def get_calender(self, id):
        try:
            professor_objs = self.get_professors().data
            for mem in professor_objs:
                if mem._id == id:
                    print(mem.first_name)
                    print(mem.office_hours)
                    return models.Result(mem.office_hours, '')
            return models.Result('', 'No data')
        except requests.exceptions.HTTPError as err:
            return models.Result('', str(err))