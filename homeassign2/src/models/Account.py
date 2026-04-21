#creating account class
from datetime import datetime
from src.models.Menu import Menu

class Account:
    def __init__ (self, runningTotals, openDate):
        self.__runningTotals = runningTotals
        self.__opendate = openDate

    def showCustomerTransactions(self, transactionList):
        for transaction in transactionList:
            print(transaction)
