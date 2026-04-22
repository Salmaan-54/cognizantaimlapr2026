# create customer json data loader implementation from customer data loader abstract class

import json
from src.models.customer import Customer
from src.models.full_name import FullName
from src.stores.customer_store_implementation import CustomerStoreImpl
from src.dataloaders.customer_data_loader import CustomerDataLoader

class CustomerJSONDataLoader(CustomerDataLoader):
    def load_data(self, file_path: str, customer_store: CustomerStoreImpl):
        with open(file_path, 'r') as f:
            data = json.load(f)
        for row in data:
            customer_id = int(row['customer_id'])
            first_name = row['first_name']
            last_name = row['last_name']
            email = row['email']
            phone_number = row['phone_number']
            customer = Customer(
                customer_id=customer_id, 
                name=FullName(first_name=first_name, last_name=last_name), 
                email=email, 
                phone_number=phone_number
            )
            customer_store.add_customer(customer)