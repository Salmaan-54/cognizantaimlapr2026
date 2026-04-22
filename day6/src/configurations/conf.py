import os
from dotenv import load_dotenv

load_dotenv()

class Conf:
    def __init__(self):
        self.url = os.getenv("URL")
    