# create customer txt data loader implementation from customer data loader abstract class

import pandas as pd
from src.models.customer import Customer
from src.models.full_name import FullName
from src.stores.customer_store_implementation import CustomerStoreImpl
from src.dataloaders.customer_data_loader import CustomerDataLoader

class CustomerTXTDataLoader(CustomerDataLoader):
    def load_data(self, file_path: str, customer_store: CustomerStoreImpl):
        with open(file_path, 'r') as f:
            raw_lines = f.readlines()
        
        lines = pd.Series([line.strip() for line in raw_lines])
        
        # Skip header
        header_end = lines.str.startswith('=').idxmax() + 1
        lines = lines[header_end:]
        
        # Filter out separators and empty lines
        valid_lines = lines[~lines.isin(['', '------------------------------', 'Customer Data', '================='])]
        
        # Group every 5 lines into customer data
        customers_data = []
        for i in range(0, len(valid_lines), 5):
            block = valid_lines.iloc[i:i+5]
            customer_id = int(block.iloc[0].split(':')[1].strip())
            first_name = block.iloc[1].split(':')[1].strip()
            last_name = block.iloc[2].split(':')[1].strip()
            email = block.iloc[3].split(':')[1].strip()
            phone_number = block.iloc[4].split(':')[1].strip()
            
            customers_data.append({
                'customer_id': customer_id,
                'first_name': first_name,
                'last_name': last_name,
                'email': email,
                'phone_number': phone_number
            })
        
        # Use pandas to create DataFrame
        df = pd.DataFrame(customers_data)
        
        # Create Customer objects from DataFrame
        for _, row in df.iterrows():
            customer = Customer(
                customer_id=int(row['customer_id']),
                name=FullName(first_name=row['first_name'], last_name=row['last_name']),
                email=row['email'],
                phone_number=row['phone_number']
            )
            customer_store.add_customer(customer)
