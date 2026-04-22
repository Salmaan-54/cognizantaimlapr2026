#configure log format
import logging
import os
"""
Set up logger for healthcare application
"""

def setup_logger(log_file: str = 'healthcare.log', logger_name: str | None = None):
    """
    Create a logger that writes to a dedicated log file.

    If no logger_name is provided, it is derived from the log file name.
    """
    if logger_name is None:
        logger_name = os.path.splitext(os.path.basename(log_file))[0]

    logger = logging.getLogger(logger_name)
    logger.setLevel(logging.DEBUG)
    logger.propagate = False

    existing_file_handler = False
    for handler in logger.handlers:
        if isinstance(handler, logging.FileHandler) and os.path.abspath(handler.baseFilename) == os.path.abspath(log_file):
            existing_file_handler = True
            break

    if existing_file_handler:
        return logger

    file_handler = logging.FileHandler(log_file)
    file_handler.setLevel(logging.DEBUG)
    formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)
    return logger