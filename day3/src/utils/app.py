import sys
import os

#Add project root to Python path
project_root = os.path.abspath(
    os.path.join(os.path.dirname(__file__), '..', '..')
)

sys.path.append(project_root)

from conf.logger_conf import setup_logger
"""
Entry point for the application. This module initializes the application and stars the main process
"""
logger = setup_logger()

def run():
    """
    test logger
    """
    logger.info("app run")

""" handle entry point """
if __name__ == "__main__":
    run()