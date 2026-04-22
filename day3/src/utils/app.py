"""Entry point for the healthcare appointment demo."""

import os
import sys

current_dir = os.path.dirname(__file__)
project_root = os.path.abspath(os.path.join(current_dir, '..', '..'))
src_root = os.path.join(project_root, 'src')

sys.path.insert(0, src_root)
sys.path.insert(0, project_root)

from conf.logger_conf import setup_logger
from src.stores.doctorstore import DoctorStore
from src.stores.patientstore import PatientStore
from src.stores.appointmentstore import AppointmentStore
from src.models.doctor import Doctor
from src.models.patient import Patient
from src.models.appointment import Appointment
from faker import Faker
from datetime import datetime, timedelta
from src.utils.displayappointments import display_appointments

logger = setup_logger("App.log")

def main():
    doctor_store = DoctorStore()
    patient_store = PatientStore()
    appointment_store = AppointmentStore()

    # Create fake data using Faker
    fake = Faker()

    # Create doctors with specialization in medical field
    specializations = ['Cardiology', 'Neurology', 'Pediatrics', 'Orthopedics', 'Dermatology', 'Psychiatry', 'Oncology', 'Gastroenterology', 'Endocrinology', 'Rheumatology', 'Pulmonology', 'Nephrology', 'Hematology', 'Infectious Disease', 'Allergy and Immunology', 'Ophthalmology', 'Otolaryngology', 'Urology', 'Gynecology', 'General Surgery']
    for i in range(10):
        doctor = Doctor(id=i+1, name=fake.name(), specialization=fake.random_element(elements=specializations))
        doctor_store.add_doctor(doctor)
    logger.info(f"Created {len(doctor_store.get_all_doctors())} doctors")

    # Create patients with ailment in medical field
    ailments = ['Diabetes', 'Hypertension', 'Asthma', 'Arthritis', 'Migraine', 'Depression', 'Anxiety', 'Cancer', 'Heart Disease', 'Stroke', 'Flu', 'Cold', 'Allergy', 'Infection', 'Back Pain', 'Skin Rash', 'Eye Infection', 'Ear Infection']
    for i in range(30):
        dob = fake.date_of_birth(minimum_age=18, maximum_age=80)
        ailment = fake.random_element(elements=ailments)
        patient = Patient(id=i+1, name=fake.name(), dob=dob, ailment=ailment)
        patient_store.add_patient(patient)
    logger.info(f"Created {len(patient_store.get_all_patients())} patients")

    # Mapping disease to specialization
    disease_specialization_map = {
        'Diabetes': 'Endocrinology',
        'Hypertension': 'Cardiology',
        'Asthma': 'Pulmonology',
        'Arthritis': 'Rheumatology',
        'Migraine': 'Neurology',
        'Depression': 'Psychiatry',
        'Anxiety': 'Psychiatry',
        'Cancer': 'Oncology',
        'Heart Disease': 'Cardiology',
        'Stroke': 'Neurology',
        'Flu': 'Infectious Disease',
        'Cold': 'Infectious Disease',
        'Allergy': 'Allergy and Immunology',
        'Infection': 'Infectious Disease',
        'Back Pain': 'Orthopedics',
        'Skin Rash': 'Dermatology',
        'Eye Infection': 'Ophthalmology',
        'Ear Infection': 'Otolaryngology'
    }

    # Create appointments with doctor, patient, date and time and mapped disease to specialization
    for i in range(30):
        patient = fake.random_element(elements=patient_store.get_all_patients())
        specialization = disease_specialization_map.get(patient.ailment, None)
        doctor = None
        if specialization:
            doctors = [doc for doc in doctor_store.get_all_doctors() if doc.specialization == specialization]
            if doctors:
                doctor = fake.random_element(elements=doctors)
        
        if doctor:
            date = datetime.now() + timedelta(days=fake.random_int(min=1, max=30))
            time = date.time()
            appointment = Appointment(id=i+1, doctor=doctor, patient=patient, date=date.date(), time=time)
            appointment_store.add_appointment(appointment)
    logger.info(f"Created {len(appointment_store.get_all_appointments())} appointments")

    # Display all appointments
    display_appointments(appointment_store)

if __name__ == "__main__":
    main()