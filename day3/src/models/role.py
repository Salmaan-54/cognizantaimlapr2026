"""
Role model definition.
"""

class Role:
    """
    A class representing a role
    """
    def __init__(self, name: str, description: str):
        self.__name = name
        self.__description = description

    #getter for name
    @property
    def get_name(self) -> str:
        return self.__name

    #getter for description
    @property
    def get_description(self) -> str:
        return self.__description

    #setter for name
    #@description.setter
    def set_description(self, description: str):
        self.__description = description