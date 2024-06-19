# WordWiz API

## Overview
WordWiz API is a web service built using JustPy that provides instant word definitions. This API allows you to integrate real-time word definitions into your applications effortlessly. With a robust backend, WordWiz API offers a reliable and scalable solution for language exploration.

## Features
- **Real-time Definitions**: Fetch instant definitions for any English word via API requests.
- **Scalable and Robust**: Built using JustPy, ensuring high performance and scalability.
- **Easy Integration**: Simple and well-documented endpoints for seamless integration into your applications.

## Project Structure
```sh
wordwiz_api_project/
│
├── config.py
│
├── definition.py
│
├── main.py
│
└── wordwiz_api.py
```

## Setup

### Prerequisites
- Python 3.x
- `pip` for managing Python packages

### Installation
1. **Clone the repository**:
    ```sh
    git clone https://github.com/yourusername/wordwiz_api.git
    cd wordwiz_api
    ```

2. **Install dependencies**:
    Ensure you have `pip` installed and use the following command to install required dependencies:
    ```sh
    pip install -r requirements.txt
    ```

3. **Configuration**:
    Modify `config.py` to set up any necessary configuration settings.

## Usage

### Running the API Server
1. **Start the server**:
    ```sh
    python main.py
    ```

2. **Access the API**:
    The API will be accessible at `http://127.0.0.1:8080` by default. You can make API requests to this endpoint to fetch word definitions.

### Example API Request
- **Endpoint**: `/wordwiz/api/v1/define`
- **Method**: GET
- **Query Parameter**: `word` (the word you want to define)

#### Example Request
```sh
curl "http://127.0.0.1:8080/wordwiz/api/v1/define?word=example"
```

#### Example Response
```json
{
    "word": "example",
    "definition": "A representative form or pattern."
}
```

### Files Description
- **config.py**: Configuration settings for the API.
- **definition.py**: Contains functions or classes related to word definitions.
- **main.py**: Entry point to start the API server.
- **wordwiz_api.py**: Contains the main API logic for handling word definition requests.