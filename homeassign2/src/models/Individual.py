from datetime import dat

class Individual(Customer):
    def __init__ (self, accountNumber, name, address, contactNumber, email, password, surname, gender, dateOfBirth):
        super().__init__(accountNumber, name, address, contactNumber, email, password)
        self.__surname = surname
        self.__gender = gender
        self.__dateOfBirth = dateOfBirth

    def workOutAge(self):
        today = datetime.today()
        age = today.year - self.__dateOfBirth.year - ((today.month, today.day) < (self.__dateOfBirth.month, self.__dateOfBirth.day))
        return age

