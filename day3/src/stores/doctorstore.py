""" create doctor crud operation"""
import sys
import os

from models.doctor import Doctor

#Add project root to Python path
project_root = os.path.abspath(
    os.path.join(os.path.dirname(__file__), '..', '..')
)

sys.path.append(project_root)

from conf.logger_conf import setup_logger
from exceptions.doctor_not_found_exception import DoctorNotFoundException

logger = setup_logger()

class DoctorStore:
    """
    DoctorStore class to manage doctor records in the healthcare application
    """
    def __init__(self):
        self.doctors = []
    
    def add_doctor(self, doctor:Doctor):
        """
        Add a doctor to the store
        """
        logger.info(f"Adding doctor: {doctor}")
        self.doctors.append(doctor)
    
    def get_doctor_by_id(self, id:int) -> Doctor:
        """
        Get a doctor by id
        """
        logger.info(f"Getting doctor by id: {id}")
        for doctor in self.doctors:
            if doctor.id == id:
                return doctor
        raise DoctorNotFoundException(f"Doctor with id {id} not found")
    
    def get_all_doctors(self) -> list:
        """
        Get all doctors in the store
        """
        logger.info("Getting all doctors")
        return self.doctors
    
    def update_doctor(self, id:int, name:str=None, specialization:str=None) -> bool:
        """
        Update a doctor's information
        """
        logger.info(f"Updating doctor with id: {id}")
        doctor = self.get_doctor_by_id(id)
        if doctor:
            if name:
                doctor.name = name
            if specialization:
                doctor.specialization = specialization
            return True
        return False

    def delete_doctor(self, id:int) -> bool:
        """
        Delete a doctor from the store
        """
        logger.info(f"Deleting doctor with id: {id}")
        doctor = self.get_doctor_by_id(id)
        if doctor:
            self.doctors.remove(doctor)
            return True
        return False