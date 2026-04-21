class Corporate(Customer):
    def __init__ (self, accountNumber, name, address, contactNumber, email, password, companyType):
        super().__init__(self, accountNumber, name, address, contactNumber, email, password)
        self.__companyType = companyType