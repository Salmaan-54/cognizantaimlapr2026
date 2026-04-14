#generate 100 cutomers and store them in a list
from faker import Faker
from model.customer import Customer

class CustomerStore:
    def __init__(self, num_customers: int):
        self.customers = self._generate_customers(num_customers)

    def _generate_customers(self, num_customers: int):
        fake = Faker()
        customers = []
        for _ in range(num_customers):
            name = fake.name()
            email = fake.email()
            dob = fake.date_of_birth().isoformat()
            customers.append(Customer(name, email, dob))
        return customers

    def get_customer(self):
        return self.customers