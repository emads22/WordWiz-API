from pathlib import Path

ASSETS = Path(__file__).parent / "assets"

RESOURCES = ASSETS / "resources"
DATA_FILE = RESOURCES / "data.csv"

# Define the API routes
BASE_URL = "http://127.0.0.1:8080"
WORDWIZ_API_ROUTE = '/wordwiz/api/v1/dictionary'
