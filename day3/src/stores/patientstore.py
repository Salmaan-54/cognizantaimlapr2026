""" create patient crud operation """

import sys
import os

#Add project root to Python path
project_root = os.path.abspath(
    os.path.join(os.path.dirname(__file__), '..', '..')
)
sys.path.append(project_root)

from conf.logger_conf import setup_logger
from exceptions.patient_not_found_exception import PatientNotFoundException
from models.patient import Patient

logger = setup_logger()

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