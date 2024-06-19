import logging
import justpy as jp
from wordwiz_api import WordWizAPI
from config import LOG_FILE


# Create the directory for log files if it doesn't exist, and Ensure parent directories are created if they don't exist
LOG_FILE.parent.mkdir(parents=True, exist_ok=True)


# Configure the logging format and level
logging.basicConfig(filename=LOG_FILE,
                    format='%(asctime)s - %(levelname)s - %(message)s (%(module)s:%(filename)s:%(lineno)d)',
                    level=logging.DEBUG)


# Register the API route with JustPy
jp.Route(WordWizAPI.path, WordWizAPI.serve)

if __name__ == "__main__":
    jp.justpy(port=8080)
