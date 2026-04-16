#configure log format
import logging
"""
Set up logger for healthcare application
"""

def setup_logger():
    """
    Create logger for healthcare application
    """
    logger = logging.getLogger('healthcare_logger')
    logger.setLevel(logging.DEBUG)

    """
    Check if logger already had handlers to avoid duplicate logs
    """
    if logger.hasHandlers():
        return logger
    
    file_handler = logging.FileHandler('healthcare.log')
    logger.setLevel(logging.DEBUG)

    """create formatter to specify log format and date format"""
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)
    return logger