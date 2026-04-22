"""
Person model
"""

import re

class Person:
    """
    A class representing a person with a name and age
    """
    def __init__(self, aadharCardNo: str, mobileNo: int):
        self.__aadharCardNo = aadharCardNo
        self.__mobileNo = mobileNo
    
    #getter for aadharCardNo
    @property
    def aadharCardNo(self) -> str:
        return self.__aadharCardNo
    
    #getter for mobileNo
    @property
    def mobileNo(self) -> int:
        return self.__mobileNo

    #setter for aadharCardNo
    @aadharCardNo.setter
    def aadharCardNo(self, aadharCardNo: str):
        self.__aadharCardNo = aadharCardNo

    #setter for mobileNo
    @mobileNo.setter
    def mobileNo(self, mobileNo: int):
        if not re.match(r'^\d{10}$', str(mobileNo)):
            raise ValueError("Invalid mobile number. It should be a 10-digit number.")
        self.__mobileNo = mobileNo  