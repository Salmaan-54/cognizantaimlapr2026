#define customer model
class Customer:
    def __init__(self, name: str, email: str, dob: str):
        self.name = name
        self.email = email
        self.dob = dob

    def __str__(self):
        return f"Customer(name={self.name}, email={self.email}, dob={self.dob})"