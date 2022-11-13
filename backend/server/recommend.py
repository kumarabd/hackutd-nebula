class Recommend:
    def __init__(self, school, subtype):
        self.school = school
        self.subtype =subtype
    def get_degree_plan(self):
        return 

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
