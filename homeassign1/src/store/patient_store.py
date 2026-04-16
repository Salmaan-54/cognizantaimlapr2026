# Generating patient data along with their disease information and storing it in a list
from faker import Faker
from model.patient import Patient


class PatientStore:
    def __init__(self, num_patients: int):
        self.patients = self._generate_patients(num_patients)

    # generating patient with common and major diseases
    def _generate_patients(self, num_patients: int):
        fake = Faker()
        # list of diseases so it aligns with the doctor specialties
        diseases = [
            "Diabetes",
            "Hypertension",
            "Asthma",
            "Cancer",
            "Heart Disease",
            "Flu",
            "Cold",
            "Allergy",
            "Migraine",
            "Arthritis",
        ]
        patients = []
        for _ in range(num_patients):
            name = fake.name()
            age = fake.random_int(min=0, max=100)
            disease = fake.random.choice(diseases)
            patients.append(Patient(name, age, disease))
        return patients

    def get_patients(self):
        return self.patients
