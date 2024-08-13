class user:
    def __init__(self,firstname,lastname,email,location):
        self.firstname=firstname
        self.lastname=lastname
        self.email=email
        self.location=location

    def to_dict(self):
        return {
            "firstname": self.firstname,
            "lastname": self.lastname,
            "email": self.email,
            "location": self.location
        }
