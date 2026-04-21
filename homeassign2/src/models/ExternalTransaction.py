class ExternalTransaction(Transaction):
    def __init__(self, amount, timeStamp, sender, receiver, branchName, branchAddress, branchPostcode, branchCode):
        super().__init__(self, amount, timeStamp, sender, receiver)
        self.__branchName = branchName
        self.__branchAddress = branchAddress
        self.__branchPostcode = branchPostcode
        self.__branchCode = branchCode