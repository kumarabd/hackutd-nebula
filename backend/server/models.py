import json

class Professor:
    calender = {}
    def __init__(self, _id, first_name,last_name,titles,email,phone_number,profile_uri,image_uri, office, office_hours, sections):
        self._id = _id
        self.first_name = first_name
        self.last_name = last_name
        self.titles = titles
        self.email = email
        self.phone_number = phone_number
        self.profile_uri = profile_uri
        self.image_uri = image_uri
        self.office = office
        self.office_hours = office_hours
        self.sections = sections

class Result:
    def __init__(self, data, error):
        self.data = data
        self.error = error
    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, 
            sort_keys=True, indent=4)
