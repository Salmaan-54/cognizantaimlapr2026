from src.models.Transaction import Transaction

class Menu:
    def __init__(self):
        self.__transactionList = []
        self.__customerAccountList = []
        self.__customerList = []
    
    def initiateTransaction(self, txn_object):
        self.__transactionList.append(txn_object)

    def addCustomer(self, accountNumber, name, address, contactNumber, email, password):
        customer = Customer(accountNumber, name, address, contactNumber, email, password)
        self.__customerList.append(customer)
    
    def deleteCustomer(self, accountNumber):
        for customer in self.__customerList:
            if customer.getAccountNumber() == accountNumber:
                self.__customerList.remove(customer)
                break
    
    def openAccount(self, accountType, runningTotals, openDate, interestRate=None, overdraftLimit=None):
        if accountType == "Saving":
            account = SavingAccount(runningTotals, openDate, interestRate)
        elif accountType == "Current":
            account = CurrentAccount(runningTotals, openDate, overdraftLimit)
        self.__customerAccountList.append(account)

    def closeAccount(self, accountNumber):
        for account in self.__customerAccountList:
            if account.getAccountNumber() == accountNumber:
                self.__customerAccountList.remove(account)
                break
    
    def editCustomerDetails(self, accountNumber, name=None, address=None, contactNumber=None, email=None, password=None):
        for customer in self.__customerList:
            if customer.getAccountNumber() == accountNumber:
                if name:
                    customer.setName(name)
                if address:
                    customer.setAddress(address)
                if contactNumber:
                    customer.setContactNumber(contactNumber)
                if email:
                    customer.setEmail(email)
                if password:
                    customer.setPassword(password)
                break
    
    def login(self, accountNumber, password):
        for customer in self.__customerList:
            if customer.getAccountNumber() == accountNumber and customer.getPassword() == password:
                return True
        return False
    
    def logout(self):
        # Implement logout functionality if needed
        pass
    