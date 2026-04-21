class SavingAccount(Account):
    def __init__(self, runningTotals, openDate, interestRate):
        super().__init__(runningTotals, openDate)
        self.__interestRate = interestRate