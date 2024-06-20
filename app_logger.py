import logging
from pathlib import Path
from config import LOG_FILE


def setup_logger(log_file: Path = LOG_FILE):
    """Set up a custom logger for the JustPy application.

    This function configures a custom logger for the JustPy application. It removes any existing log handlers,
    creates a custom logger instance, sets its logging level to DEBUG, adds file and console handlers,
    and applies a formatter to format log messages.

    Args:
        log_file (Path, optional): The path to the log file. Defaults to the value specified in the LOG_FILE constant.

    Returns:
        logging.Logger: The configured custom logger instance.

    """
    # Ensure that the directory for the log file exists otherwise create it
    log_file.parent.mkdir(parents=True, exist_ok=True)

    # Clear existing log handlers
    # We iterate over a copy of the list of handlers associated with the root logger to safely remove each handler.
    # Using a copy of the list with [:] ensures that we're not modifying the original list while iterating over it.
    # So we ensure that each handler is correctly processed and removed,
    # without affecting the original list of handlers associated with the root logger.
    for handler in logging.root.handlers[:]:
        logging.root.removeHandler(handler)

    # Create a custom logger
    # Get or create a logger instance with the name of the root logger.
    logger = logging.getLogger()
    # Set the logging level of the custom logger to DEBUG, indicating that all log messages of DEBUG level or higher will be processed.
    logger.setLevel(logging.DEBUG)  # Set to desired level

    # Create handlers
    # Create a FileHandler to write log messages to a file specified by log_file.
    file_handler = logging.FileHandler(log_file)
    # Set the logging level of the FileHandler to DEBUG to process all log messages.
    file_handler.setLevel(logging.DEBUG)

    # Create formatters and add them to handlers
    # Create a formatter with a specific format for log messages.
    this_format = '%(asctime)s - %(levelname)s - %(message)s (%(module)s:%(filename)s:%(lineno)d)'
    formatter = logging.Formatter(this_format)

    # Set the formatter for the FileHandler to format log messages.
    file_handler.setFormatter(formatter)

    # Add handlers to the logger
    # Add the FileHandler to the custom logger to handle log messages by writing them to the specified file.
    logger.addHandler(file_handler)

    return logger
