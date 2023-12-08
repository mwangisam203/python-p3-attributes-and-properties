class Dog:
    approved_breeds = ["Labrador Retriever", "German Shepherd", "Golden Retriever", "French Bulldog"]

    def __init__(self, name="", breed=""):
        self._name = ""
        self._breed = ""
        self.name = name
        self.breed = breed

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str) or not (1 <= len(value) <= 25):
            print("Name must be a string between 1 and 25 characters.")
        else:
            self._name = value

    @property
    def breed(self):
        return self._breed

    @breed.setter
    def breed(self, value):
        if value not in Dog.approved_breeds:
            print("Breed must be in the list of approved breeds.")
        else:
            self._breed = value
