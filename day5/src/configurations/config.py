#create configuration file for the project

import os
from dotenv import load_dotenv
load_dotenv()

class Config():
    def __init__(self):
        self.app_env = os.getenv("APP_ENV")
        self.resource_path = self.get_resource_path()

    def get_resource_path(self) -> str:
        if self.app_env == "Production":
            return "src/resources/customers.json"
        elif self.app_env == "Development":
            return "src/resources/customers.csv"
        else:
            return "src/resources/customers.txt"