# patient details and their assigned doctor details are displayed in this view
class PatientView:
    def __init__(self, patient_doctor_map: dict):
        self.patient_doctor_map = patient_doctor_map

    def display_patient_doctor_mapping(self):
        for patient, doctor in self.patient_doctor_map.items():
            doctor_info = (
                f"{doctor.name} ({doctor.specialty})"
                if doctor
                else "No doctor assigned"
            )
            print(
                f"{patient.name} (Age: {patient.age}, Disease: {patient.disease}) -> {doctor_info}"
            )
