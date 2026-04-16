"""
Create appointment
"""

from datetime import date, time
from models.doctor import Doctor
from models.patient import Patient

class Appointment:
    """
    Appointment class
    """
    def __init__(self, id:int, doctor:Doctor, patient:Patient, date:date, time:time):
        self.appointment_id = id
        self.doctor = doctor
        self.patient = patient
        self.date = date
        self.time = time

    def __str__(self):
        return f"Appointment(id={self.appointment_id}, doctor={self.doctor}, patient={self.patient}, date='{self.date}', time='{self.time}')"