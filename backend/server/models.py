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

class Degree:
    def __init__(self, _id, school, subtype, name, year, abbreviation, minimum_credit_hours, catalog_uri, requirements):
        self._id = _id
        self.school = school
        self.subtype = subtype
        self.name = name
        self.year = year
        self.abbreviation = abbreviation
        self.minimum_credit_hours = minimum_credit_hours
        self.catalog_uri = catalog_uri
        self.requirements = requirements

class Course:
    def __init__(self, _id, course_number, subject_prefix, title, description, school, credit_hours, class_level, activity_type, grading, internal_course_number, lecture_contact_hours, offering_frequency, co_or_pre_requisites, corequisites, laboratory_contact_hours, prerequisites, sections):
        self._id = _id
        self.course_number = course_number
        self.subject_prefix = subject_prefix
        self.title = title
        self.description = description
        self.school = school
        self.credit_hours = credit_hours
        self.class_level = class_level
        self.activity_type = activity_type
        self.grading = grading
        self.internal_course_number = internal_course_number
        self.lecture_contact_hours = lecture_contact_hours
        self.offering_frequency = offering_frequency
        self.co_or_pre_requisites = co_or_pre_requisites
        self.corequisites = corequisites
        self.laboratory_contact_hours = laboratory_contact_hours
        self.prerequisites = prerequisites
        self.sections = sections
