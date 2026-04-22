"""
test for doctor contract
"""
#get absolute path of doctor.py
import os
import sys
import pytest
import csv

project_root = os.path.abspath(
    os.path.join(os.path.dirname(__file__), '..', '..')
)
sys.path.append(project_root)

from src.models.doctor import Doctor

@pytest.fixture
def initialize_doctor():
    doctor = Doctor(id=1, name="Dr. Smith", specialization="Cardiology")
    return doctor

def read_doctors_from_csv():
    doctors = []
    with open("./tests/doctors.csv", mode='r', newline='', encoding='utf-8') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            doctors.append((int(row['id']), row['name'], row['specialization']))
    return doctors

def test_doctor_creation(initialize_doctor):
    doctor = initialize_doctor
    assert doctor.name == "Dr. Smith"
    assert doctor.specialization == "Cardiology"

def test_doctor_str(initialize_doctor):
    doctor = initialize_doctor
    assert str(doctor) == "Doctor(id=1, name='Dr. Smith', specialization='Cardiology')"

@pytest.mark.parametrize("id, name, specialization", read_doctors_from_csv()) 

def test_parameterized_doctor_creation(id, name, specialization):
    doctor = Doctor(id=id, name=name, specialization=specialization)
    assert doctor.id == id
    assert doctor.name == name
    assert doctor.specialization == specialization