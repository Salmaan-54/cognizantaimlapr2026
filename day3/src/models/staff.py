"""
create class staff inherit from person class and associated to role as attribute
"""

from src.models.person import Person
from src.models.role import Role
class Staff(Person):
    """
    Staff class representing a staff member in the healthcare application
    """
    def __init__(self, aadharCardNo: str, mobileNo: int, role: Role):
        super().__init__(aadharCardNo, mobileNo)
        self.role = role

    @property
    def role(self):
        return self.__role
    
    @role.setter
    def role(self, role: Role):
        self.__role = role

    def __str__(self):
        return f"Staff(aadharCardNo={self.get_aadharCardNo()}, mobileNo={self.get_mobileNo()}, role={self.role})"