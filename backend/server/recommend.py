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

class Recommend:
    def __init__(self, school, subject_prefix, class_level):
        self.school = school
        self.subject_prefix = subject_prefix
        self.class_level = class_level
    def get_degree_plan(self):
        degree_objs = []
        try:
            response = requests.get(API_URL+'/degree/',headers=HEADERS)
            response.raise_for_status()
            j = json.loads(response.text)
            for mem in j['data']:
                degree_objs.append(models.Degree(**mem))
            return models.Result(degree_objs, '')
        except requests.exceptions.HTTPError as err:
            return models.Result('', str(err))
    def get_courses(self):
        course_objs = []
        try:
            response = requests.get(API_URL+'/course/',headers=HEADERS)
            response.raise_for_status()
            j = json.loads(response.text,object_hook=remove_v)
            for mem in j['data']:
                course_objs.append(models.Course(**mem))
            return models.Result(course_objs, '')
        except requests.exceptions.HTTPError as err:
            return models.Result('', str(err))
    def get_options(self, course_objs):
        schools = []
        class_levels = []
        subject_prefixs = []
        try:
            for c in course_objs:
                schools.append(c.school)
                class_levels.append(c.class_level)
                subject_prefixs.append(c.subject_prefix)
            schools = list(set(schools))
            class_levels = list(set(class_levels))
            subject_prefixs = list(set(subject_prefixs))
            return models.Result({
                'schools' : schools,
                'class_levels' : class_levels,
                'subject_prefixs' : subject_prefixs
            }, '')
        except requests.exceptions.HTTPError as err:
            return models.Result('', str(err))