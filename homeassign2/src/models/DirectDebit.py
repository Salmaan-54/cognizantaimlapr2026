class DirectDebit(Transaction):
    def __init__(self, amount, timeStamp, sender, receiver, paymentDate):
        super().__init__(self, amount, timeStamp, sender, receiver)
        self.__paymentDate = paymentDate