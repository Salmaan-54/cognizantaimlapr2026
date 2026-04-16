"""
create patient not found exception
"""

class PatientNotFoundException(Exception):
    """
    Custom exception to handle cases where a patient is not found in the healthcare application
    """
    def __init__(self, message="Patient not found"):
        self.message = message
        super().__init__(self.message)
    
    def __str__(self):
        return f"PatientNotFoundException: {self.message}"