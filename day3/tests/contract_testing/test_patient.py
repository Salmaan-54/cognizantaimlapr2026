"""
test for patient contract
"""

#get absolute path of patient.py
import csv
import os
import sys
import pytest

project_root = os.path.abspath(
    os.path.join(os.path.dirname(__file__), '..', '..')
)
sys.path.append(project_root)

from src.models.patient import Patient 
@pytest.fixture
def initialize_patient():
    patient = Patient(id=1, name="John Doe", dob="1990-01-01", ailment="Flu")
    return patient

def read_patients_from_csv():
    patients = []
    with open("./tests/patients.csv", mode='r', newline='', encoding='utf-8') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            patients.append((int(row['id']), row['name'], row['dob'], row['ailment']))
    return patients

def test_patient_creation(initialize_patient):
    patient = initialize_patient
    assert patient.name == "John Doe"
    assert patient.ailment == "Flu"

def test_patient_str(initialize_patient):
    patient = initialize_patient
    assert str(patient) == "Patient(id=1, name='John Doe', dob='1990-01-01', ailment='Flu')"

@pytest.mark.parametrize("id, name, dob, ailment", read_patients_from_csv())
def test_parameterized_patient_creation(id, name, dob, ailment):
    patient = Patient(id=id, name=name, dob=dob, ailment=ailment)
    assert patient.id == id
    assert patient.name == name
    assert patient.dob == dob
    assert patient.ailment == ailment
