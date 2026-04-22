"""
write test case for doctor not found exception
"""

import os
import sys
import pytest

project_root = os.path.abspath(
    os.path.join(os.path.dirname(__file__), '..', '..')
)
sys.path.append(project_root)

from src.exceptions.doctor_not_found_exception import DoctorNotFoundException
from src.stores.doctorstore import DoctorStore

def test_doctor_not_found_exception():
    doctor_store = DoctorStore()
    with pytest.raises(DoctorNotFoundException) as exc_info:
        doctor_store.get_doctor_by_id(999)  # Assuming 999 is an ID that does not exist
    assert str(exc_info.value) == "Doctor with id 999 not found."