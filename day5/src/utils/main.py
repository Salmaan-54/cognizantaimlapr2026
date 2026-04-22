# Display the customers 

import os
import sys
from faker import Faker

# Add project root directory to Python path
project_root = os.path.abspath(
    os.path.join(os.path.dirname(__file__), '..', '..')
)
sys.path.append(project_root)

from src.configurations.config import Config
from src.dataloaders.customer_csv_data_loader import CustomerCSVDataLoader
from src.dataloaders.customer_json_data_loader import CustomerJSONDataLoader
from src.dataloaders.customer_txt_data_loader import CustomerTXTDataLoader
from src.stores.customer_store_implementation import CustomerStoreImpl
from src.utils.pipeline_runner import PipelineRunner

# def display_customers():
#     config = Config()
#     env = config.app_env
#     if env == "Development":
#         customer_loader = CustomerCSVDataLoader()
#         customer_store = CustomerStoreImpl()
#         customer_loader.load_data(config.resource_path, customer_store)
        
#         for customer in customer_store.get_all_customers():
#             print(f"Customer ID: {customer.customer_id}, Name: {customer.name}, Email: {customer.email}, Phone: {customer.phone_number}")
#     elif env == "Production":
#         customer_loader = CustomerJSONDataLoader()
#         customer_store = CustomerStoreImpl()
#         customer_loader.load_data(config.resource_path, customer_store)
        
#         for customer in customer_store.get_all_customers():
#             print(f"Customer ID: {customer.customer_id}, Name: {customer.name}, Email: {customer.email}, Phone: {customer.phone_number}")
#     elif env == "Testing":
#         customer_loader = CustomerTXTDataLoader()
#         customer_store = CustomerStoreImpl()
#         customer_loader.load_data(config.resource_path, customer_store)
        
#         for customer in customer_store.get_all_customers():
#             print(f"Customer ID: {customer.customer_id}, Name: {customer.name}, Email: {customer.email}, Phone: {customer.phone_number}")
#     else:
#         print("Invalid environment specified in configuration.")

def load_customers(**kwargs):
    customer_store = kwargs['customer_store']
    config = Config()
    env = config.app_env
    if env == "Development":
        customer_loader = CustomerCSVDataLoader()
        customer_loader.load_data(config.resource_path, customer_store)
    elif env == "Production":
        customer_loader = CustomerJSONDataLoader()
        customer_loader.load_data(config.resource_path, customer_store)
    elif env == "Testing":
        customer_loader = CustomerTXTDataLoader()
        customer_loader.load_data(config.resource_path, customer_store)
    else:
        print("Invalid environment specified in configuration.")
    
def display_customers(**kwargs):
    customer_store = kwargs['customer_store']
    for customer in customer_store.get_all_customers():
        print(f"Customer ID: {customer.customer_id}")
        print(f"Name: {customer.name}")
        print(f"Email: {customer.email}")
        print(f"Phone: {customer.phone_number}")
        print()

def update_customer(**kwargs):
    customer_store = kwargs['customer_store']
    customer_id = kwargs['customer_id']
    customer = customer_store.get_customer(customer_id)
    fake = Faker()
    customer.name.first_name = fake.first_name()
    customer.name.last_name = fake.last_name()
    customer.email = fake.email()
    customer.phone_number = fake.phone_number()
    customer_store.update_customer(customer_id, customer)
    return customer_store

def delete_customer(**kwargs):
    customer_store = kwargs['customer_store']
    customer_id = kwargs['customer_id']
    customer_store.delete_customer(customer_id)


def get_customer_by_id(**kwargs):
    customer_store = kwargs['customer_store']
    customer_id = kwargs['customer_id']
    customer = customer_store.get_customer_by_id(customer_id)
    print(f"Customer ID: {customer.customer_id}")
    print(f"Name: {customer.name}")
    print(f"Email: {customer.email}")
    print(f"Phone: {customer.phone_number}")
    # return customer_store.get_customer_by_id(customer_id)


if __name__ == "__main__":
    customer_store = CustomerStoreImpl()
    pipeline_runner = PipelineRunner()
    pipeline_runner.add_stage(load_customers)
    pipeline_runner.add_stage(display_customers)
    pipeline_runner.add_stage(update_customer)
    pipeline_runner.add_stage(get_customer_by_id)
    pipeline_runner.add_stage(delete_customer)
    pipeline_runner.add_stage(display_customers)
    pipeline_runner.run(customer_store=customer_store, customer_id=8)