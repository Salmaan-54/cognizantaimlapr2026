"""
create doctor not found exception
"""

class DoctorNotFoundException(Exception):
    """
    Custom exception to handle cases where a doctor is not found in the healthcare application
    """
    def __init__(self, message="Doctor not found"):
        self.message = message
        super().__init__(self.message)
    
    def __str__(self):
        return f"DoctorNotFoundException: {self.message}"
    
    