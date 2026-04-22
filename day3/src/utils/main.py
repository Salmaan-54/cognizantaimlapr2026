import sys
import os

project_root = os.path.abspath(
    os.path.join(os.path.dirname(__file__), '..', '..')
)
sys.path.append(project_root)

from src.models.person import Person
from src.models.staff import Staff
from src.models.role import Role

from conf.logger_conf import setup_logger

logger = setup_logger("Main.log")

def create_person() -> Person:
    """
    Create a person object
    """
    person = Person(aadharCardNo="1234-5678-9012-3456", mobileNo="9876543210")
    # person.set_aadharCardNo("0987-6543-2109-8765")
    # person.set_mobileNo(123405678)
        
    print(f"Creating person with aadharCardNo: {person.aadharCardNo}, mobileNo: {person.mobileNo}")
    
    try:
        person.mobileNo = 9123456
        logger.info("Mobile number set successfully")
    except ValueError as e:
        logger.error(f"Error setting mobile number: {e}")

    return person

def create_staff():
    """
    Create a staff object
    """
    role = Role(name="Nurse", description="A healthcare professional who provides care to patients")
    staff = Staff(aadharCardNo="1234-5678-9012-3456", mobileNo=9876543210, role=role)
    print(f"Creating staff with aadharCardNo: {staff.aadharCardNo}, mobileNo: {staff.mobileNo}, role: {staff.role}")
    return staff

if __name__ == "__main__":
    create_person()
