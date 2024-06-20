from pathlib import Path

ASSETS = Path(__file__).parent / "assets"
LOG_FILE = ASSETS / "log" / "app.log"
DATA_FILE = ASSETS / "resources" / "data.csv"

# Define the API routes
BASE_URL = "http://127.0.0.1:8080"
WORDWIZ_API_ROUTE = '/wordwiz/api/v1/define'
