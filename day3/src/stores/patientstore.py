"""Patient CRUD operations."""

from conf.logger_conf import setup_logger
from src.exceptions.patient_not_found_exception import PatientNotFoundException
from src.models.patient import Patient

logger = setup_logger("PatientStore.log")

class PatientStore:
    """
    PatientStore class to manage patient records in the healthcare application
    """
    def __init__(self):
        self.patients = []
    
    def add_patient(self, patient:Patient):
        """
        Add a patient to the store
        """
        logger.info(f"Adding patient: {patient}")
        self.patients.append(patient)
    
    def get_patient_by_id(self, id:int) -> Patient:
        """
        Get a patient by id
        """
        logger.info(f"Getting patient by id: {id}")
        for patient in self.patients:
            if patient.id == id:
                return patient
        raise PatientNotFoundException(f"Patient with id {id} not found")
    
    def get_all_patients(self) -> list:
        """
        Get all patients in the store
        """
        logger.info("Getting all patients")
        return self.patients
    
    def update_patient(self, id:int, name:str=None, age:int=None) -> bool:
        """
        Update a patient's information
        """
        logger.info(f"Updating patient with id: {id}")
        patient = self.get_patient_by_id(id)
        if patient:
            if name:
                patient.name = name
            if age:
                patient.age = age
            return True
        raise PatientNotFoundException(f"Patient with id {id} not found")