import logging
import pandas as pd
from config import DATA_FILE


# Retrieve or create a logger instance associated with the current module name.
# This ensures that each module has its own logger, facilitating modular logging
# and allowing for easier tracking of log messages to their respective modules.
logger = logging.getLogger(__name__)


class Definition:
    """
    A class to retrieve definitions for a given term from a DataFrame.
    """

    def __init__(self, term: str) -> None:
        """
        Initializes the Definition object with the given term.

        Parameters:
        - term (str): The term for which definitions will be retrieved.
        """
        self.term = term.lower()  # to be case insensitive
        self.df = None
        try:
            self.df = pd.read_csv(DATA_FILE)
        except FileNotFoundError as e:
            logger.error(f"Data file '{DATA_FILE}' not found: {e}")

    def get(self) -> list:
        """
        Retrieves definitions for the given term.

        Returns:
        - list: A list of definitions for the term.
        """
        if self.df is None:
            return []  # Return an empty list if DataFrame is not initialized

        try:
            # Filter the DataFrame to get definitions for the given term
            definitions = self.df.loc[self.df['word']
                                      == self.term]['definition'].tolist()
            return definitions

        except KeyError as e:
            logger.error(f"Key error occurred: {e}")
            return []  # Return an empty list if the term is not found in the DataFrame
