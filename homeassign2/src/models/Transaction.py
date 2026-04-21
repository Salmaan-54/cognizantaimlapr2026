class Transaction:
    def __init__(self, amount, timeStamp, sender, receiver):
        self.__amount = amount
        self.__timeStamp = timeStamp
        self.__sender = sender
        self.__receiver = receiver
    
    def depositMoney(self, amount):
        self.__amount += amount
    
    def withdrawMoney(self, amount):
        self.__amount -= amount