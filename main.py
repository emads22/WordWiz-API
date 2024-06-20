import logging
import justpy as jp
from app_logger import setup_logger
from wordwiz_api import WordWizAPI


# Set up custom logger
logger = setup_logger()

# Register the API route with JustPy
jp.Route(WordWizAPI.path, WordWizAPI.serve)

if __name__ == "__main__":
    logging.debug("debug logging test")
    logging.error("error logging test")
    jp.justpy(port=8080)
