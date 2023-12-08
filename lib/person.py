class Person:
    approved_jobs = ["Engineer", "Doctor", "Teacher", "Software Developer"]

    def __init__(self, name="", job=""):
        self._name = ""
        self._job = ""
        self.name = name
        self.job = job

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str) or not (1 <= len(value) <= 25):
            print("Name must be a string under 25 characters.")
        else:
            self._name = value.title()

    @property
    def job(self):
        return self._job

    @job.setter
    def job(self, value):
        if value not in Person.approved_jobs:
            print("Job must be in the list of approved jobs.")
        else:
            self._job = value
