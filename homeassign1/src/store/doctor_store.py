# generating doctor specialist in diseases and storing it in a list
from faker import Faker
from model.doctor import Doctor


class DoctorStore:
    def __init__(self, num_doctors: int):
        self.doctors = self._generate_doctors(num_doctors)

    # generating doctor with major and common specialties
    def _generate_doctors(self, num_doctors: int):
        fake = Faker()
        # list of specialties so it aligns with the all patient diseases
        specialties = [
            "Endocrinology",
            "Cardiology",
            "Pulmonology",
            "Oncology",
            "Endocrinology",
            "General Medicine",
            "Allergy and Immunology",
            "Neurology",
            "Rheumatology",
            "Gastroenterology",
        ]
        doctors = []
        for _ in range(num_doctors):
            name = fake.name()
            specialty = fake.random.choice(specialties)
            doctors.append(Doctor(name, specialty))
        return doctors

    def get_doctors(self):
        return self.doctors
