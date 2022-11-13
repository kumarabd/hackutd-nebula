import json
import requests
import os
import models

API_URL = 'https://api.utdnebula.com'
HEADERS = {'content-type': 'application/json', 'x-api-key': os.environ['API_KEY']}

def remove_v(dct):
    if '__v' in dct:
        dct.pop('__v', None)
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
        professor_objs = []
        #Add dummy professor
        dummy_office = {
            "building": "ecs",
            "room": "2.308",
            "map_uri": "none"
        }
        dummy_office_hours = {
            "start_date": "January 18, 2022",
            "end_date": "May 5, 2022",
            "meeting_days": "Monday",
            "start_time": "10:00am",
            "end_time": "11:15am",
            "modality": "traditional",
            "building": "SLC",
            "room": "2.203"
        }
        dummy_sections = []
        dummy_titles = []
        dummy_prof = models.Professor("000000000000000000000000", "dum", "my", dummy_titles, "dummy@dummy.com", "0000000000", "none", "none", dummy_office, dummy_office_hours, dummy_sections)
        professor_objs.append(dummy_prof)
        try:
            response = requests.get(API_URL+'/professor/',headers=HEADERS)
            response.raise_for_status()
            j = json.loads(response.text,object_hook=remove_v)
            for mem in j['data']:
                professor_objs.append(models.Professor(**mem))
            return models.Result(professor_objs, '')
        except requests.exceptions.HTTPError as err:
            return models.Result('', str(err))
    
    def get_calender(self, professor_objs, id):
        try:
            if not professor_objs:
                professor_objs = self.get_professors().data
            for mem in professor_objs:
                print(mem)
                if mem._id == id:
                    return models.Result(mem.office_hours, '')
            return models.Result('', 'No data')
        except requests.exceptions.HTTPError as err:
            return models.Result('', str(err))