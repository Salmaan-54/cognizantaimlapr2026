#create customer store implementation from customer store abstract class

from src.exceptions.customer_not_found import CustomerNotFoundException
from src.stores.customer_store import CustomerStore

class CustomerStoreImpl(CustomerStore):
    def __init__(self):
        self.customer = []

    def add_customer(self, customer):
        self.customer.append(customer)
    
    def get_customer(self, customer_id):
        for customer in self.customer:
            if customer.customer_id == customer_id:
                return customer
        raise CustomerNotFoundException(customer_id)

    def update_customer(self, customer_id, customer):
        for i in range(len(self.customer)):
            if self.customer[i].customer_id == customer_id: 
                self.customer[i] = customer
                return True
        raise CustomerNotFoundException(customer_id)
    
    def delete_customer(self, customer_id):
        for i in range(len(self.customer)):
            if self.customer[i].customer_id == customer_id:
                del self.customer[i]
                return True
        raise CustomerNotFoundException(customer_id)

    def get_all_customers(self):
        return self.customer
            
    def get_all_customers(self):
        return self.customer