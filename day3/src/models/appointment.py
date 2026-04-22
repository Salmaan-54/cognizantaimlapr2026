"""
Create appointment
"""

from datetime import date, time
from src.models.doctor import Doctor
from src.models.patient import Patient

class Appointment:
    """
    Appointment class
    """
    def __init__(self, id:int, doctor:Doctor, patient:Patient, date:date, time:time):
        self.id = id
        self.doctor = doctor
        self.patient = patient
        self.date = date
        self.time = time

    def __str__(self):
        return f"Appointment(id={self.id}, doctor={self.doctor}, patient={self.patient}, date='{self.date}', time='{self.time}')"