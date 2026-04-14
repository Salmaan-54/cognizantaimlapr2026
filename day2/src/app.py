# creating entry point for the application

import faker
from store.customerstore import CustomerStore
from view.customerview import CustomerView
from model.customer import Customer
from datetime import date
"""
    creating entry point for the application to display a random name.
"""

def check():
    #Initilize the customer store with 100 customers
    customer_store = CustomerStore(100)
    #Initilize the customer view with the customer store
    customer_view = CustomerView(customer_store)
    #Display the customers
    customer_view.display_customers()

if __name__ == "__main__":
    check()