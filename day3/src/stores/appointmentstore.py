"""Appointment store."""

from src.models.appointment import Appointment
from conf.logger_conf import setup_logger

logger = setup_logger("AppointmentStore.log")

class AppointmentStore:
    """
    AppointmentStore class to manage appointment records in the healthcare application
    """
    def __init__(self):
        self.appointments = []
    
    def add_appointment(self, appointment:Appointment):
        """
        Add an appointment to the store
        """
        logger.info(f"Adding appointment: {appointment}")
        self.appointments.append(appointment)
    
    def get_appointment_by_id(self, id:int) -> Appointment:
        """
        Get an appointment by id
        """
        logger.info(f"Getting appointment by id: {id}")
        for appointment in self.appointments:
            if appointment.id == id:
                return appointment
        return None
    
    def get_all_appointments(self) -> list:
        """
        Get all appointments in the store
        """
        logger.info("Getting all appointments")
        return self.appointments