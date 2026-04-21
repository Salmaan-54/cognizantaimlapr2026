# Display the customers 

import os
import sys

# Add project root directory to Python path
project_root = os.path.abspath(
    os.path.join(os.path.dirname(__file__), '..', '..')
)
sys.path.append(project_root)

from src.configurations.config import Config
from src.dataloaders.customer_csv_data_loader import CustomerCSVDataLoader
from src.stores.customer_store_implementation import CustomerStoreImpl

def display_customers():
    config = Config()
    env = config.app_env
    if env == "Development":
        customer_loader = CustomerCSVDataLoader()
        customer_store = CustomerStoreImpl()
        customer_loader.load_data(config.resource_path, customer_store)
        
        for customer in customer_store.get_all_customers():
            print(f"Customer ID: {customer.customer_id}, Name: {customer.name}, Email: {customer.email}, Phone: {customer.phone_number}")

if __name__ == "__main__":
    display_customers()