# WordWiz API

## Overview
WordWiz API is a web service built using JustPy that provides instant word definitions. This API allows you to integrate real-time word definitions into your applications effortlessly. With a robust backend, WordWiz API offers a reliable and scalable solution for language exploration.

## Features
- **Real-time Definitions**: Fetch instant definitions for any English word via API requests.
- **Scalable and Robust**: Built using JustPy, ensuring high performance and scalability.
- **Easy Integration**: Simple and well-documented endpoints for seamless integration into your applications.
- **Custom Logger**: Easily add a custom logger to track and manage application logs efficiently. Users are free to adjust custom logging settings by modifying the `setup_logger` function according to their requirements.

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

## Contributing
Contributions are welcome! Here are some ways you can contribute to the project:
- Report bugs and issues
- Suggest new features or improvements
- Submit pull requests with bug fixes or enhancements

## Author
- Emad &nbsp; E>
  
  [<img src="https://img.shields.io/badge/GitHub-Profile-blue?logo=github" width="150">](https://github.com/emads22)

## License
This project is licensed under the MIT License, which grants permission for free use, modification, distribution, and sublicense of the code, provided that the copyright notice (attributed to [emads22](https://github.com/emads22)) and permission notice are included in all copies or substantial portions of the software. This license is permissive and allows users to utilize the code for both commercial and non-commercial purposes.

Please see the [LICENSE](LICENSE) file for more details.