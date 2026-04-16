"""
create patient
"""
import typing
from datetime import date
class Patient:
    """
    Patient class to represent a patient in the healthcare application
    """
    def __init__(self, id:int, name:str, dob:date, ailment:str):
        self.id = id
        self.name = name
        self.dob = dob
        self.ailment = ailment
    
    def __str__(self):
        return f"Patient(id={self.id}, name='{self.name}', dob='{self.dob}', ailment='{self.ailment}')"