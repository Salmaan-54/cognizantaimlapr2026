class CurrentAccount(Account):
    def __init__(self, runningTotals, openDate, overdraftLimit):
        super().__init__(runningTotals, openDate)
        self.__overdraftLimit = overdraftLimit