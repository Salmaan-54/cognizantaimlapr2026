#creating entry point for the application
from faker import Faker
from model.doctor import Doctor
from model.patient import Patient
from store.doctor_store import DoctorStore
from store.patient_store import PatientStore
from store.patient_doctor_map import PatientDoctorMap
from view.patient_view import PatientView

def main():
    # Using already created patient, doctor and mapping stores to generate data and display it
    num_patients = 40
    num_doctors = 20
    patient_store = PatientStore(num_patients)
    doctor_store = DoctorStore(num_doctors)
    patient_doctor_map = PatientDoctorMap(patient_store.get_patients(), doctor_store.get_doctors())
    patient_view = PatientView(patient_doctor_map.get_patient_doctor_map())
    patient_view.display_patient_doctor_mapping()

if __name__ == "__main__":
    main()