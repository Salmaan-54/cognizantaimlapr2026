#create customer csv data loader implementation from customer data loader abstract class

import pandas as pd
from src.models.customer import Customer
from src.models.full_name import FullName
from src.stores.customer_store_implementation import CustomerStoreImpl
from src.dataloaders.customer_data_loader import CustomerDataLoader

class CustomerCSVDataLoader(CustomerDataLoader):
    def load_data(self, file_path: str, customer_store: CustomerStoreImpl):
            data = pd.read_csv(file_path)
            for _, row in data.iterrows():
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