# mapping patient to doctor according to their disease and doctor's specialty
from model.patient import Patient
from model.doctor import Doctor


class PatientDoctorMap:
    def __init__(self, patients: list[Patient], doctors: list[Doctor]):
        self.patient_doctor_map = self._map_patients_to_doctors(patients, doctors)

    def _map_patients_to_doctors(self, patients: list[Patient], doctors: list[Doctor]):
        # mapping diseases to specialties
        disease_specialty_map = {
            "Diabetes": "Endocrinology",
            "Hypertension": "Cardiology",
            "Asthma": "Pulmonology",
            "Cancer": "Oncology",
            "Heart Disease": "Cardiology",
            "Flu": "General Medicine",
            "Cold": "General Medicine",
            "Allergy": "Allergy and Immunology",
            "Migraine": "Neurology",
            "Arthritis": "Rheumatology",
        }
        patient_doctor_map = {}
        for patient in patients:
            specialty = disease_specialty_map.get(patient.disease)
            doctor = next((doc for doc in doctors if doc.specialty == specialty), None)
            patient_doctor_map[patient] = doctor
        return patient_doctor_map

    def get_patient_doctor_map(self):
        return self.patient_doctor_map
