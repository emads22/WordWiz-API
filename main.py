import justpy as jp
from app_logger import AppLogger
from wordwiz_api import WordWizAPI


# Initialize an AppLogger instance
app_logger = AppLogger().logger


# Register the API route with JustPy
jp.Route(WordWizAPI.path, WordWizAPI.serve)


if __name__ == "__main__":

    try:
        jp.justpy(port=8080)

    except Exception:
        # Log the exception with stack trace (automatically without passing {e} cz `logger.exception()`)
        app_logger.exception("An unexpected error occurred")
