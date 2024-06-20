import logging
import json
import justpy as jp
from definition import Definition
from config import WORDWIZ_API_ROUTE


# Retrieve or create a logger instance associated with the current module name.
# This ensures that each module has its own logger, facilitating modular logging
# and allowing for easier tracking of log messages to their respective modules.
logger = logging.getLogger(__name__)


class WordWizAPI:
    """
    Handles requests at http://127.0.0.1:8080/wordwiz-api/v1/define?word=

    Retrieves definitions for the given word and returns them in JSON format.
    """

    path = WORDWIZ_API_ROUTE

    @classmethod
    def serve(cls, request):
        """
        Serves the WordWizAPI endpoint.

        Retrieves definitions for the given word and returns them in JSON format.

        Parameters:
        - request (justpy.Request): The request object.

        Returns:
        - justpy.WebPage: The response WebPage object.
        """
        try:
            wp = jp.WebPage()

            try:
                # Retrieve definitions for the specified word by calling the `get()` method of the Definition class
                # The `word` parameter is extracted from the GET request's query parameters
                word = request.query_params.get('word')
                definitions = Definition(word).get()
            except Exception as e:
                # Log the error
                logger.error(
                    f"Error while retrieving definitions for '{word}': {e}")
                return

            # Construct the response dictionary
            response = {
                'word': word,
                'definitions': definitions if definitions else None
            }

            # Convert the dictionary to JSON format
            json_response = json.dumps(response)

            # Set the HTML content of the response WebPage to the JSON-formatted response obtained from the API
            # This allows the JSON response to be rendered as HTML content on the webpage
            wp.html = json_response

            return wp

        except Exception:
            # Log any exceptions using the custom logger
            logger.exception("An exception occurred")
