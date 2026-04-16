# define doctor model
class Doctor:
    def __init__(self, name: str, specialty: str):
        self.name = name
        self.specialty = specialty

    def __str__(self):
        return f"Doctor(name={self.name}, specialty={self.specialty})"
