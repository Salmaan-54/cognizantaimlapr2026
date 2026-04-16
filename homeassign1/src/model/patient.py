# define patient model
class Patient:
    def __init__(self, name: str, age: int, disease: str):
        self.name = name
        self.age = age
        self.disease = disease

    def __str__(self):
        return f"Patient(name={self.name}, age={self.age}, disease={self.disease})"
